import json

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from user.models import Profile
from feeds.models import Feed
from decorators import ajax_required
# from bootcamp.articles.models import Article


@login_required
def search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q').strip()
        if len(querystring) == 0:
            return redirect('/search/')

        try:
            search_type = request.GET.get('type')
            if search_type not in ['feed', 'users']:
                search_type = 'feed'

        except Exception:
            search_type = 'feed'

        count = {}
        results = {}
        results['feed'] = Feed.objects.filter(post__icontains=querystring,
                                              parent=None)
        results['users'] = Profile.objects.filter(
            Q(username__icontains=querystring) | Q(
                first_name__icontains=querystring) | Q(
                    last_name__icontains=querystring))
        count['feed'] = results['feed'].count()
        # count['articles'] = results['articles'].count()
        count['users'] = results['users'].count()

        return render(request, 'search/results.html', {
            'hide_search': True,
            'querystring': querystring,
            'active': search_type,
            'count': count,
            'results': results[search_type],
        })

    else:
        return render(request, 'search/search.html', {'hide_search': True})


# For autocomplete suggestions
@login_required
@ajax_required
def get_autocomplete_suggestions(request):
    querystring = request.GET.get('term', '')
    # Convert users, articles objects into list to be
    # represented as a single list.
    users = list(Profile.objects.filter(
        Q(username__icontains=querystring) | Q(
            first_name__icontains=querystring) | Q(
                last_name__icontains=querystring)))

    # Add all the retrieved users, articles to data_retrieved
    # list.
    data_retrieved = users
    results = []
    for data in data_retrieved:
        data_json = {}

        if isinstance(data, Profile):
            data_json['id'] = data.id
            data_json['label'] = data.username
            data_json['value'] = data.username

        results.append(data_json)

    final_suggestions = json.dumps(results)

    return HttpResponse(final_suggestions, 'application/json')
