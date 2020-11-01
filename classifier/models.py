from django.db import models

# Create your models here.
class Portrait(models.Model):
    name = models.CharField(max_length=50)
    portrait_img = models.ImageField(upload_to='images/')