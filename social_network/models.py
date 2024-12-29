from django.db import models

from common.models import BaseModel


class SiteModel(BaseModel):
    site_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Sayt nomi")
    location = models.CharField(max_length=200, null=True, blank=True, verbose_name="Servis manzili")
    email = models.EmailField(null=True, blank=True, verbose_name="Elektron pochta manzili")
    telegram_bot = models.CharField(max_length=200, null=True, blank=True, verbose_name="Telegram bot manzili")
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name="Telefon raqami")
    facebook = models.CharField(max_length=200, null=True, blank=True, verbose_name="Facebook manzili")
    instagram = models.CharField(max_length=200, null=True, blank=True, verbose_name="Instagram manzili")
    youtube = models.CharField(max_length=200, null=True, blank=True, verbose_name="Youtube manzili")

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Sayt ma'lumotlari"
        verbose_name = "Sayt ma'lumotlari"
