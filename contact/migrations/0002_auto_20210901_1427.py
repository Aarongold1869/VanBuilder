# Generated by Django 3.0.14 on 2021-09-01 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactsubmission',
            old_name='content',
            new_name='message',
        ),
    ]