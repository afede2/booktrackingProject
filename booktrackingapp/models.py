from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    pages = models.IntegerField()

    def __str__(self):
        return f"Book: '{self.name}' - '{self.author}' - '{self.description}' - {self.pages}"


#class Author(models.Model):
#    name = models.CharField(max_length=50)

#class User(models.Model):
#    name = models.CharField(max_length=50)
#    email = models.EmailField()
#    password = models.CharField(max_length=50)



