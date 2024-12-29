from django.db import models

from common.models import BaseModel


class BaseCarouselModel(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Sarlavha')
    description = models.TextField(verbose_name='Matn')
    background_image = models.ImageField(upload_to='carousel', verbose_name='Asosiy rasm')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Asosiy Karusel'
        verbose_name_plural = 'Asosiy Karusellar'
