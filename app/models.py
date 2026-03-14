from django.db import models


class Contact(models.Model):
    name = models.CharField()
    course = models.CharField(null=True, blank=True)
    phone_number = models.CharField()

    def __str__(self):
        return self.name

class Mentor(models.Model):
    name = models.CharField()
    image = models.ImageField()
    job = models.CharField()

class Portfolio(models.Model):
    image = models.ImageField()
    title = models.CharField()
    image_author = models.ImageField(null=True, blank=True)
    author = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.title
