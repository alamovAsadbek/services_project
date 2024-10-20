from django.db import models


class SocialNetworkModel(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Ijtimoiy tarmoqlar"
        verbose_name = "Ijtimoiy tarmoq"
