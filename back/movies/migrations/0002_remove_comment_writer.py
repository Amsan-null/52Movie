# Generated by Django 3.2 on 2023-11-21 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='writer',
        ),
    ]