from django.db import models

# Create your models here.

class Login(models.Model):
    uname=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    user_type=models.CharField(max_length=200)
    def __str__(self):
        return self.uname

class Package(models.Model):
    title=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='package')
    description=models.CharField(max_length=2000)
    def __str__(self):
        return self.title