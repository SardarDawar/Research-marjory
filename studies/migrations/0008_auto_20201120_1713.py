# Generated by Django 3.1.3 on 2020-11-20 12:13

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0007_auto_20201120_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replica',
            name='entrypoint',
            field=models.CharField(max_length=50, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()]),
        ),
    ]
