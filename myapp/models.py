from django.db import models

# Create your models here.

from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    linkedin_url = models.URLField(max_length=200)
