from django.db import models


class SocialNetworkModel(models.Model):
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.instagram

    class Meta:
        verbose_name_plural = "Ijtimoiy tarmoqlar"
        verbose_name = "Ijtimoiy tarmoq"
