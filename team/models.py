from PIL import Image as PilImage
from django.core.exceptions import ValidationError
from django.db import models

from common.models import BaseModel


# validation
def validate_image_format(image):
    try:
        img = PilImage.open(image)
        if img.format not in ['JPEG', 'JPG', 'PNG']:
            raise ValidationError('Image must be in JPEG or PNG format.')
    except Exception:
        raise ValidationError('Invalid image file.')


def validate_image_dimensions(image):
    img = PilImage.open(image)
    if img.size != (300, 300):
        raise ValidationError('Image dimensions must be exactly 300x300 pixels.')


class TeamModel(BaseModel):
    first_name = models.CharField(max_length=80, verbose_name='Ism')
    last_name = models.CharField(max_length=80, verbose_name='Familiya')
    profession = models.CharField(max_length=100, verbose_name='Mutaxassislik')
    image = models.ImageField(upload_to='team', blank=True, null=True,
                              validators=[validate_image_dimensions, validate_image_format], verbose_name='Rasm')
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
