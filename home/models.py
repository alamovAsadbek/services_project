from django.db import models

from common.models import BaseModel


class BaseCarouselModel(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel')
