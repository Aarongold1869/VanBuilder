# Generated by Django 3.0.14 on 2021-08-29 19:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0003_auto_20210809_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='build',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
