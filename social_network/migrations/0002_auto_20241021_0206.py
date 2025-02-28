# Generated by Django 3.2.9 on 2024-10-20 21:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('site_name', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': "Sayt ma'lumotlari",
                'verbose_name_plural': "Sayt ma'lumotlari",
            },
        ),
        migrations.AddField(
            model_name='socialnetworkmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='socialnetworkmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
