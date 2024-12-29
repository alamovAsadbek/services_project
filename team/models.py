from PIL import Image as PilImage
from django.core.exceptions import ValidationError
from django.db import models

from common.models import BaseModel


# validation
def validate_image_format(image):
    try:
        img = PilImage.open(image)
        if img.format not in ['JPEG', 'JPG', 'PNG']:
            raise ValidationError("Rasm JPEG yoki PNG formatida bo'lishi kerak.")
    except Exception:
        raise ValidationError("Rasm fayli yaroqsiz.")


def validate_image_dimensions(image, max_width: int = 300, max_height: int = 300):
    img = PilImage.open(image)
    if img.size != (max_width, max_height):
        raise ValidationError(f"Rasm o'lchamlari aniq {max_width}x{max_height} piksel bo'lishi kerak.")


def validate_image_dimensions_review(image, max_width: int = 100, max_height: int = 100):
    img = PilImage.open(image)
    if img.size != (max_width, max_height):
        raise ValidationError(f"Rasm o'lchamlari aniq {max_width}x{max_height} piksel bo'lishi kerak.")


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
    first_name = models.CharField(max_length=80, verbose_name='Ism')
    last_name = models.CharField(max_length=80, verbose_name='Familiya')
    description = models.TextField(verbose_name="Sharh matni")
    image = models.ImageField(upload_to='reviews',
                              validators=[validate_image_dimensions_review, validate_image_format], blank=True,
                              null=True, verbose_name='Rasm')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Sharh'
        verbose_name_plural = 'Sharhlar'
