# Generated by Django 3.2 on 2023-11-21 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_comment_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rating',
        ),
    ]