from django.db import models

from common.models import BaseModel


class AboutUs(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to='about_us')
    image2 = models.ImageField(upload_to='about_us')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Kompaniyaning Haqida"
        verbose_name = "Kompaniya Haqida"
