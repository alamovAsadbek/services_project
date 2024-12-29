from django.db import models

from common.models import BaseModel


class AboutUsModel(BaseModel):
    title = models.CharField(max_length=200, verbose_name='Sarlavha')
    description = models.TextField(verbose_name='Matn')
    image1 = models.ImageField(upload_to='about_us', verbose_name='Rasm1')
    image2 = models.ImageField(upload_to='about_us', verbose_name='Rasm2')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Kompaniyaning Haqida"
        verbose_name = "Kompaniya Haqida"
