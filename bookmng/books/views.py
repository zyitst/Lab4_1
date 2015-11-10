#from django.shortcuts import render
from django.shortcuts import render_to_response
from books.models import Book, Author
from django.template import Context, RequestContext
from django.http import *
#from django.http import HttpResponse

def search(request):
    errors = []
    if 'Author' in request.GET:
        au_name = request.GET['Author']
        if not au_name:
            errors.append('Please enter a search term!')
        else:
            auth_name_list = []
            for auth in Author.objects.all():
                auth_name_list.append(auth.Name)
            if au_name in auth_name_list:
                author_id = Author.objects.get(Name=au_name).AuthorID
                books = Book.objects.filter(AuthorID=author_id)
                return render_to_response('search_result.html', {'books': books, 'query': au_name})
            else:
                errors.append('No author found!')
    return render_to_response('search.html',{'errors': errors})

def book_info(request):
    if 'ISBN' in request.GET:
        tISBN = request.GET['ISBN']
        book_info = Book.objects.get(ISBN=tISBN)
        Author_info=book_info.AuthorID
#        Author_info = Author.objects.get(AuthorID=tAuthorID)
        return render_to_response('book_info.html', {'book_info': book_info, 'Author_info': Author_info})
    else:
        return HttpResponse("No ISBN Found!")

def del_a_book(request):
    tISBN = request.GET['ISBN']
    tAuthorID = request.GET['AuID']
    book = Book.objects.get(ISBN=tISBN)
    book.delete()
    books = Book.objects.filter(AuthorID=Author.objects.get(Name=tAuthorID))
    return render_to_response('search_result.html', {'books': books})
'''
def add_book(request):
    if request.POST:
        post = request.POST
        auth_id_list = []
        msg = []
        for author in Author.objects.all():
            auth_id_list.append(author.AuthorID)
        if post["AuthorID"] in auth_id_list:
            new_book = Book(
                ISBN = post["ISBN"],
                Title = post["Title"],
#                AuthorID = Author.objects.get(AuthorID=post["AuthorID"]),
                Publisher = post["Publisher"],
                PublishDate = post["PublishDate"],
                Price = post["Price"])
            new_book.save()
            msg.append("Book added successfully!")
            return render_to_response("add_book.html", {'msg': msg}, context_instance=RequestContext(request))
        else:
            msg.append("Author doesn't exist!")
            return render_to_response("add_book.html", {'msg': msg}, context_instance=RequestContext(request))
    else:
        return render_to_response("add_book.html")
#def add_author(request):
'''
