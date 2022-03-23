from django.db import models

# Create your models here.
class hydjobs(models.Model):
    Date = models.DateField()
    Company = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Eligibility = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Email = models.EmailField()
    Phonenumber = models.IntegerField()

class banglorejobs(models.Model):
    Date = models.DateField()
    Company = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Eligibility = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Email = models.EmailField()
    Phonenumber = models.IntegerField()

class chennaijobs(models.Model):
    Date = models.DateField()
    Company = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Eligibility = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Email = models.EmailField()
    Phonenumber = models.IntegerField()

class punejobs(models.Model):
    Date = models.DateField()
    Company = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Eligibility = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Email = models.EmailField()
    Phonenumber = models.IntegerField()