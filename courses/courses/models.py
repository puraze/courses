from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class student(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.TextField()
