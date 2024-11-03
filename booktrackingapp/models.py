from django.db import models

#
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.email}"


#model containing all authors present in the books database,  currently not in
#use but could be incorporated in future to allow user to search by author
class Author(models.Model):
    name = models.CharField(max_length=50)
    genera = models.CharField(max_length=50)

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    #artist = models.ForeignKey(Author, related_name="books", \
    #                           on_delete=models.CASCADE)
    description = models.TextField()
    pages = models.IntegerField()

    def __str__(self):
        return f"Book: '{self.name}' - '{self.author}' - '{self.description}' - {self.pages}"

class UserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book= models.ForeignKey(Book, on_delete=models.CASCADE)
    statues = models.IntegerField() #e.g 1 'to read', 2 'in progress', 3 'did not finish', 4 'completed'
    def __str__(self):
        return f"{self.user} - {self.book}"

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    journal_entry = models.TextField()
    entry_date = models.DateField()
    def __str__(self):
        return f"{self.user} - {self.book} - '{self.journal_entry}' - {self.entry_date}"



