# Generated by Django 3.2.9 on 2024-10-24 05:06

from django.db import migrations, models
import team.models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammodel',
            name='facebook_url',
            field=models.URLField(blank=True, help_text='Bu yerda Facebook akkauntini link kurinishda berish kerak', null=True, verbose_name='Facebook URL'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='first_name',
            field=models.CharField(max_length=80, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='team', validators=[team.models.validate_image_dimensions, team.models.validate_image_format], verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='instagram_url',
            field=models.URLField(blank=True, help_text='Bu yerda Instagram akkauntini link kurinishda berish kerak', null=True, verbose_name='Instagram URL'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='last_name',
            field=models.CharField(max_length=80, verbose_name='Familiya'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='profession',
            field=models.CharField(max_length=100, verbose_name='Mutaxassislik'),
        ),
    ]
