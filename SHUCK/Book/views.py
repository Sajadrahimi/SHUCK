from django.http import HttpResponse

from .models import Author


# Return Books of an Author
def showAuthorBooks(request, AuthorName) :
    print("SHOW AUTHOR BOOKS CALLED \t", AuthorName)
    if request.method == 'GET' :
        if Author.isAuthorExists(AuthorName) :
            return HttpResponse(Author.getAuthorBooks(AuthorName))
        else :
            return HttpResponse("Not Found")
