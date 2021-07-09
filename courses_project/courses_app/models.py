from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField

# Create your models here.

class courseManager(models.Manager):
    def courseValidator(self, postData):
        errors = {}
        if len(postData['course_name']) < 5:
            errors['course_name'] = "Name must be at least 5 characters."
        if len(postData['description']) < 15:
            errors['description'] = "Description must be at least 15 characters."
        return errors


class Description(models.Model):
    body = models.TextField() # remember its description.BODY not description.DESCRIPTION!!
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = courseManager()