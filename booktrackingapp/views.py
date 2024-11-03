from django.shortcuts import render, HttpResponse
from . models import Book, UserBook, JournalEntry

# Create your views here.
def index(request):
    books = Book.objects.all()
    user_books = UserBook.objects.all()
    journal_entries = JournalEntry.objects.all()

    return render(request, 'index.html', {'books': books, 'user_books': user_books, 'journal_entries': journal_entries})


def in_progress_book(request, user_id):
    #query all books in UserBook database for specified user statues 1, 'in progress'
    in_progress_books = UserBook.objects.filter(user_id=user_id, status=1)

    #pass to template
    return render(request, 'index.html', {'in_progress_books': in_progress_books})
