from django.db import models


class Contact(models.Model):
    name = models.CharField()
    course = models.CharField(null=True, blank=True)
    phone_number = models.CharField()

class Mentor(models.Model):
    name = models.CharField()
    image = models.ImageField()
    job = models.CharField()