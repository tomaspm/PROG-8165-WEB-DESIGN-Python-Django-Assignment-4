from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    category=models.TextField()
class Transactions(models.Model):
    dateoftrans=models.DateField()
    description=models.TextField()
    transcategory=models.TextField()
    amount=models.TextField()


def __str__(self):
    return self.user.username
