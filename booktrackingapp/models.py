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

class BookStatues(models.Model):
    TO_READ = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    DID_NOT_FINISH = 3

class BookRating(models.Model):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

class UserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book= models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.IntegerField(default=BookStatues.TO_READ)
    rating = models.IntegerField(default=BookRating.ZERO)
    def __str__(self):
        return f"{self.user} - {self.book} - ({self.get_status_display()}) - ({self.get_rating_display()})"

    def get_status_display(self):
        status_mapping = {
            BookStatues.TO_READ: "To Read",
            BookStatues.IN_PROGRESS: "In Progress",
            BookStatues.COMPLETED: "Completed",
            BookStatues.DID_NOT_FINISH: "Did Not Finish",
        }

        return status_mapping[self.status]

    def get_rating_display(self):
        rating_mapping = {
            BookRating.ZERO: "0",
            BookRating.ONE: "1",
            BookRating.TWO: "2",
            BookRating.THREE: "3",
            BookRating.FOUR: "4",
            BookRating.FIVE: "5",
        }
        return rating_mapping[self.rating]



class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    journal_entry = models.TextField()
    entry_date = models.DateField()
    def __str__(self):
        return f"{self.user} - {self.book} - '{self.journal_entry}' - {self.entry_date}"



