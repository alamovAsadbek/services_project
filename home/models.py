from django.db import models


class BaseCarouselModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel')
