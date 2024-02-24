from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

class Authors(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    born_date = models.CharField(max_length=150, null=False)
    born_location = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=10000, null=False)

    def __str__(self):
        return f"{self.fullname}"

class Quotes(models.Model):
    tags = models.CharField(max_length=500, null=False)
    author = models.CharField(max_length=50, null=False)
    quote = models.CharField(max_length=500, null=False)

    def __str__(self):
        return f"{self.tags}"
