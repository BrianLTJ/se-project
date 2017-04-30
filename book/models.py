from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group, User

# Create your models here.
class Category(models.Model):
    text = models.CharField(max_length=50)
    note = models.TextField(null=True, default="", blank=True)

    def __str__(self):
        return self.text


class Tag(models.Model):
    text = models.CharField(max_length=50)
    note = models.TextField(null=True,default="", blank=True)

    def __str__(self):
        return self.text


class Book(models.Model):
    bookid = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=20)
    cover = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=500)
    translator = models.CharField(max_length=500, null=True,default="", blank=True)
    edition = models.CharField(max_length=20)
    pubhouse = models.CharField(max_length=50)
    pubtime = models.CharField(max_length=20)
    summary = models.TextField(null=True,default="", blank=True)
    context = models.TextField(null=True,default="", blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    clc = models.CharField(max_length=20)

    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)

    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class LibBook(models.Model):
    libbookid = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book)
    barid = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=150)
    borrowuser = models.ForeignKey(User, null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class BookOperation(models.Model):
    libbook=models.ForeignKey(LibBook)
    operation=models.CharField(max_length=10)
    operator = models.ForeignKey(User, null=True, blank=True, related_name="operator")
    user = models.ForeignKey(User, related_name="borrowuser")
    operationtime = models.DateTimeField(auto_now_add=True)


class BorrowRight(models.Model):
    group = models.ForeignKey(Group)
    booknum = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    allowborrow = models.BooleanField(default=False)

