from lib2to3.fixes.fix_input import context
from urllib import request

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from . models import Book, UserBook, JournalEntry
from .forms import EntryForm


# Create your views here.
def index(request):
    books = Book.objects.all()
    user_books = UserBook.objects.all()
    journal_entries = JournalEntry.objects.all()

    return render(request, 'index.html', {'books': books, 'user_books': user_books, 'journal_entries': journal_entries})

@login_required
def add_to_list(request):
    userbook = request.user #Logged In Person
    #print(userbook)

    #Get Changed Variables
    for book in Book.objects.all():
        rating = request.POST.get(f'rating_{book.id}')
        status = request.POST.get(f'status_{book.id}')
        print(status, rating)
        #Check for changed Status & Rating for attached book ID
        if status and rating:
            #Check to see if book already in saved list or not
            if UserBook.objects.filter(book_id=book.id, user_id=userbook.id):
                #print('Book saved already exists')
                changeBook = UserBook.objects.get(book_id=book.id, user_id=userbook.id)
                changeBook.status = status
                changeBook.rating = rating
                changeBook.save()
                print('Saved new status and rating')
            # Create new entry if there isn't an existing one for specified book and user
            else:
                newbook = UserBook()
                newbook.book_id = book.id
                newbook.user_id = userbook.id
                newbook.status = status
                newbook.rating = rating
                newbook.save()
                print('New entry made successfully')

            print(f'Book: {book.name},ID:{book.id}; Status: {status}; Rating: {rating}')

            #Redirect to Selected Page
            ##Redirect to-read page
            print(status)
            if status == '0':
                print("Going to to read")

                return redirect(to_read)
            ##Redirect to in-progress page
            elif status == '1':
                print("Going to in progress")

                return redirect(in_progress)
            ##Redirect to journal entry page
            elif status == '2':
                print("Going to completed")

                return redirect(completed)
            elif status == '3':
                print("Unfinished")
                return redirect(index)


@login_required
def to_read(request):
    #query all books in UserBook database for specified user statues 0, 'to read'
    to_read_books = UserBook.objects.filter(user_id=request.user.id, status=0)

    #pass to template
    return render(request, 'to-read.html', context={'to_read_books': to_read_books})

@login_required
def in_progress(request):
    #query all books in UserBook database for specified user statues 1, 'in progress'
    #print("Now at In-Progress page")
    in_progress_books = UserBook.objects.filter(user_id=request.user.id, status=1)

    #pass to template
    return render(request, 'in-progress.html', {'in_progress_books': in_progress_books})

@login_required
def completed(request):
    #query all books in UserBook database for specified user statues 2, 'completed'
    completed_books = UserBook.objects.filter(user_id=request.user.id, status=2)

    #pass to template
    return render(request, 'completed.html', {'completed_books': completed_books})

@login_required
def stats(request):
    #query elements of the user reading stats such as pages read per book,
    # total books read, and average rating

    completed_books = UserBook.objects.filter(user_id=request.user.id, status=2)
    all_books = Book.objects.all()
    pages_read = 0
    books_read = 0
    average_rating = 0
    for done_book in completed_books:
        books_read += 1
        for book in all_books:
            if done_book.book_id == book.id:
                pages_read += book.pages
                average_rating += done_book.rating
    average_rating = average_rating / books_read

    return render(request, 'stats.html', {'pages_read': pages_read, 'books_read': books_read, 'average_rating': average_rating})

@login_required
def journal_entry(request):
    try:
        all_books = Book.objects.all()
        for book in all_books:
            selected_book = request.POST.get(f'book_chosen_{book.id}')
            if selected_book:
                selected_book = UserBook.objects.filter(book_id=selected_book, user_id=request.user.id)
                print(request.POST.get(f'book_chosen_{book.id}'))

                booksJournalEntries = JournalEntry.objects.filter(book_id=request.POST.get(f'book_chosen_{book.id}'), user_id=request.user.id)
                print(booksJournalEntries)

                newEntry = EntryForm()
                return render(request, 'journal_entry.html', {'journal_entries': booksJournalEntries, 'selected_book': selected_book, 'newEntry': newEntry})
    except ValueError:
        return HttpResponse('Invalid input')



@login_required()
def create_entry(request):
    userbook = request.POST.get('chosen_book_id')
    entry_description = request.POST.get('journal_entry')

    print(f'{userbook}, {entry_description}')
    #entry = EntryForm(request.POST)
    #if entry.is_valid():
    #    entry.user_id = request.user.id
    #    entry.book_id = userbook
    #    entry.journal_entry = entry_description
    #    entry.save()
    journal = JournalEntry(book_id=userbook, user_id=request.user.id, journal_entry=entry_description).save()

    return JsonResponse({'success': True, 'entry_description':entry_description})
