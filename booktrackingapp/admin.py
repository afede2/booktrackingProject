from django.contrib import admin
from booktrackingapp.models import Book, UserBook, JournalEntry

# Register your models here.

admin.site.register(Book)
admin.site.register(UserBook)
admin.site.register(JournalEntry)