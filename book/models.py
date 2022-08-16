from django.db import models
class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey('book.Author', on_delete=models.CASCADE)
    libraries = models.ManyToManyField('book.Library')

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        name = self.first_name
        last_name = self.last_name
        fullname = name + " " + last_name

        return fullname


class Lead(models.Model):

    email = models.EmailField(max_length=100, unique=True)
    fullname = models.CharField(max_length=100)
    phone = models.IntegerField()
    library = models.ForeignKey('book.Library', on_delete=models.CASCADE)

def __str__(self):
    return self.name