# Generated by Django 3.1.3 on 2020-11-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0009_auto_20201120_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='replica',
            name='save_uncompleted_scripts',
            field=models.BooleanField(default=True),
        ),
    ]