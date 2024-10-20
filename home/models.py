from django.db import models

from common.models import BaseModel


class BaseCarouselModel(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(upload_to='carousel')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Asosiy Karusel'
        verbose_name_plural = 'Asosiy Karusellar'
