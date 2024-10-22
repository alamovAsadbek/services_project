from django.db import models

from common.models import BaseModel


class ServiceModel(BaseModel):
    title = models.CharField(max_length=255, unique=True, verbose_name="Xizmat nomi")
    description = models.TextField(verbose_name="Xizmat haqida ma'lumot")
    image = models.ImageField(upload_to='services', verbose_name="Xizmat rasmi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Xizmat narxi")
    is_active = models.BooleanField(default=True, verbose_name="Faol xizmat")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Xizmatlarimiz"
        verbose_name = "Xizmat"


class FeatureModel(BaseModel):
    title = models.CharField(max_length=255, unique=True, verbose_name="Xususiyat nomi")
    description = models.TextField(verbose_name="Xususiyat haqida ma'lumot")
    image = models.ImageField(upload_to='features', verbose_name="Xususiyat rasmi")
    is_active = models.BooleanField(default=True, verbose_name="Faol xususiyat")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Xususiyatlari"
        verbose_name = "Xususiyat"


class WorkModel(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Qilgan ishingiz nomi")
    description = models.TextField(verbose_name="Qilgan ishingiz haqida ma'lumot")
    image = models.ImageField(upload_to='works', verbose_name="Qilgan ishingiz rasmi")
    is_active = models.BooleanField(default=True, verbose_name="Faol ish")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Ishlarimiz"
        verbose_name = "Ish"
