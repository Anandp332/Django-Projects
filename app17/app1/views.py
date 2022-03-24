from django.http import HttpResponse
from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app1.models import Book


def insertBooks(request):
    a, b, c = '', 100, 500.0
    for i in range(1, 100):
        a = "Book" + str(i)
        b += i
        c += i
        book = Book(name=a, nop=b, cost=c)
        print(book)
        book.save()
    return HttpResponse('<h1>Inserted</h1>')


def index(request):
    book_list = Book.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(book_list, 10)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, 'book_list.html', {'books': books})
