from django.db import models


class Myuser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    # Add more fields as needed


class Student(models.Model):
    studentname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=False, blank=False)


class Courses(models.Model):
    coursename = models.CharField(max_length=100)
    description = models.TextField()


class Record(models.Model):
    studentname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    objects = None
