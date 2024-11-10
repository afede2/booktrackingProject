from django.shortcuts import render, HttpResponse, redirect
from . models import Book, BookStatues, BookRating, User, JournalEntry

# Create your views here.
def index(request):
    books = Book.objects.all()
    #user_books = UserBook.objects.all()
    journal_entries = JournalEntry.objects.all()

#    return render(request, 'index.html', {'books': books, 'user_books': user_books, 'journal_entries': journal_entries})

#def to_read_book(request, user_id):
    #query all books in UserBook database for specified user statues 0, 'to read'
    #to_read_books = UserBook.objects.filter(user_id=user_id, status=0)

    #pass to template
 #   return render(request, 'to-read.html', {'to_read_books': to_read_books})

#def in_progress_book(request, user_id):
    #query all books in UserBook database for specified user statues 1, 'in progress'
    #in_progress_books = UserBook.objects.filter(user_id=user_id, status=1)

    #pass to template
#    return render(request, 'in-progress.html', {'in_progress_books': in_progress_books})

#def completed_book(request, user_id):
    #query all books in UserBook database for specified user statues 2, 'completed'
    #completed_books = UserBook.objects.filter(user_id=user_id, status=2)

 #   #pass to template
 #   return render(request, 'completed.html', {'completed_books': completed_books})
