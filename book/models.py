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
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class BookBorrow(models.Model):
    libbook = models.ForeignKey(LibBook)
    operator = models.ForeignKey(User, null=True, blank=True, related_name="operator")
    user = models.ForeignKey(User, related_name="borrowuser")
    borrowtime = models.DateTimeField(auto_now_add=True)
    returntime = models.DateTimeField(null=True,blank=True)
    # borrowtype 借书类型 b 普通借书 e 续期，同一个libbook对应同一个user，同一时间只能有一个未关闭的e，仅在该libbook和该user
    borrowtype = models.CharField(default='b', max_length=6)
    # return type 归还类型 n 未还， e 被展期，r 已还
    returntype = models.CharField(default='n', max_length=6)
