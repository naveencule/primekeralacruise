from django.db import models

# Create your models here.

class Login(models.Model):
    uname=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    user_type=models.CharField(max_length=200)
    def __str__(self):
        return self.uname