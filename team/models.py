from django.db import models

from common.models import BaseModel


class TeamModel(BaseModel):
    first_name = models.CharField(max_length=80, verbose_name='Ism')
    last_name = models.CharField(max_length=80, verbose_name='Familiya')
    profession = models.CharField(max_length=100, verbose_name='Mutaxassislik')
    image = models.ImageField(upload_to='team', blank=True, null=True, verbose_name='Rasm')
    facebook_url = models.URLField(blank=True, null=True, verbose_name='Facebook URL',
                                   help_text="Bu yerda Facebook akkauntini link kurinishda berish kerak")
    instagram_url = models.URLField(blank=True, null=True, verbose_name='Instagram URL',
                                    help_text="Bu yerda Instagram akkauntini link kurinishda berish kerak")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'


class ReviewModel(BaseModel):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(upload_to='reviews', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Sharh'
        verbose_name_plural = 'Sharhlar'
