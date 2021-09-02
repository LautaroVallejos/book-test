from django.db import models


class Library(models.Model):

    name = models.CharField(max_length=100)


class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey('book.Author', on_delete=models.CASCADE)
    libraries = models.ManyToManyField('book.Library')


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Lead(models.Model):

    email = models.EmailField(max_length=100)
    fullname = models.CharField(max_length=100)
    phone = models.SmallIntegerField()
    library = models.ForeignKey('book.Library', on_delete=models.CASCADE)

def __str__(self):
    return self.name