# Generated by Django 3.2 on 2023-11-21 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password_confirmation',
            new_name='passwordConfirmation',
        ),
    ]