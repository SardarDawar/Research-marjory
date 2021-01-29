# Generated by Django 3.1.3 on 2020-11-19 08:09

import common.storage
from django.db import migrations, models
import studies.models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0005_auto_20201119_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='content',
            field=models.ImageField(max_length=500, storage=common.storage.OverwriteStorage(), upload_to=studies.models.replicaImageSavePath),
        ),
    ]
