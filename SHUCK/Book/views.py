from django.http import HttpResponse
from django.template import loader

from .models import Author

def AddBook(request):
    if request.method == 'GET':
        return HttpResponse("Add Book Was Here")
def getBookDetail(request):

    return HttpResponse('Book/book.html',{

    })
def getAuthorBooks_form(request) :
    template = loader.get_template('Book/getAuthorBooks.html')
    return HttpResponse(template.render({}, request))

def showAuthorBooks(request, AuthorName):
    print("SHOW AUTHOR BOOKS CALLED \t", AuthorName)
    if request.method == 'GET':
        if  Author.isAuthorExists(AuthorName):
            return HttpResponse(Author.getAuthorBooks(AuthorName))
        else:
            return HttpResponse("Not Found")

def showAuthor(request):
    return HttpResponse(Author.getAuthorBooks("AuthorTest"))
