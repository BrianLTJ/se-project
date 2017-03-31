from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__:
        return name


class Category(models.Model):
    text = models.CharField(max_length=50)
    note = models.TextField(null=True)

    def __str__:
        return text


class Tag(models.Model):
    text = models.CharField(max_length=50)
    note = models.TextField(null=True)

    def __str__:
        return text


class Book(models.Model):
    bookid = models.AutoField(primary_key=TGrue)
    cover = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    translator = models.ManyToManyField(Author)
    edition = models.CharField(max_length=20)
    pubhouse = models.CharField(max_length=50)
    pubtime = models.CharField(max_length=20)
    summary = models.TextField(null=True)
    context = models.TextField(null=True)
    price = models.
    clc = models.CharField(max_length=20)

    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)

    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)



class LibBook(models.Model):
    libbookid = models.AutoField(primary_key=True)
    barid = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
