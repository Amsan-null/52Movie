# Generated by Django 4.2.7 on 2023-11-17 06:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.FloatField(default=2.5, validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(5.0)]),
            preserve_default=False,
        ),
    ]