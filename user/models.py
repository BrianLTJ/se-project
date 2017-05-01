from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.
class BorrowRight(models.Model):
    name = models.CharField(null=True, blank=True)
    booknum = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    allowborrow = models.BooleanField(default=False)


class UserBorrowRight(models.Model):
    user = models.ForeignKey(User)
    borrowright = models.ForeignKey(BorrowRight)

