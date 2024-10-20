from django.db import models

from common.models import BaseModel


class SocialNetworkModel(BaseModel):
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.instagram

    class Meta:
        verbose_name_plural = "Ijtimoiy tarmoqlar"
        verbose_name = "Ijtimoiy tarmoq"


class SiteNameModel(BaseModel):
    site_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Sayt nomlari"
        verbose_name = "Sayt nomi"
