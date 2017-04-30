from django.db import models
from django.contrib.auth.models import Group

# Create your models here.

class BorrowRight(models.Model):
    group = models.OneToOneField(Group)
    booknum = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    allowborrow = models.BooleanField(default=False)