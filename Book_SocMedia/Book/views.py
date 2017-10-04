from django.http import HttpResponse


def AddBook(request):
    if request.method == 'GET':
        return HttpResponse("Add Book Was Here")
