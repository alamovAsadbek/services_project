from django.db import models

from common.models import BaseModel


class TeamModel(BaseModel):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team', blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'
