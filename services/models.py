from PIL import Image as PILImage
from django.core.exceptions import ValidationError
from django.db import models

from common.models import BaseModel


def validate_image(image):
    if image.size > 2 * 1024 * 1024:
        raise ValidationError("Rasm o'lchami 2MB dan kichik bo'lishi kerak.")

    if not image.name.endswith(('.png', '.jpg', '.jpeg')):
        raise ValidationError("Rasm faqat .png, .jpg yoki .jpeg formatida bo'lishi kerak.")
    img = PILImage.open(image)
    if img.size != (600, 400):
        raise ValidationError("Rasm o'lchami 600x400 piksel bo'lishi kerak.")


class ServiceModel(BaseModel):
    title = models.CharField(max_length=255, unique=True, verbose_name="Xizmat nomi")
    description = models.TextField(verbose_name="Xizmat haqida ma'lumot")
    image = models.ImageField(upload_to='services', verbose_name="Xizmat rasmi", validators=[validate_image])
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Xizmat narxi")
    is_active = models.BooleanField(default=True, verbose_name="Faol xizmat")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Xizmatlarimiz"
        verbose_name = "Xizmat"


class FeatureModel(BaseModel):
    title = models.CharField(max_length=255, unique=True, verbose_name="Qulaylik nomi")
    description = models.TextField(verbose_name="Qulaylik haqida ma'lumot")
    image = models.ImageField(upload_to='features', verbose_name="Qulaylik rasmi")
    is_active = models.BooleanField(default=True, verbose_name="Faol xususiyat")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Qulayliklarimiz"
        verbose_name = "Qulaylik"


class WorkModel(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Qilgan ishingiz nomi")
    description = models.TextField(verbose_name="Qilgan ishingiz haqida ma'lumot")
    image = models.ImageField(upload_to='works', verbose_name="Qilgan ishingiz rasmi")
    is_active = models.BooleanField(default=True, verbose_name="Faol ish")
    who_did = models.ForeignKey('team.TeamModel', on_delete=models.SET_NULL, null=True,
                                verbose_name="Bu ishni kim bajargan", related_name='works',
                                description="Agar bu ishni jamoa bilan birga qilingan bo'linsa, hech nima "
                                            "tanlanmasa o'zi jamoa bilan bo'lib tanlanadi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Ishlarimiz"
        verbose_name = "Ish"
