# Generated by Django 3.1.3 on 2020-11-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0003_auto_20201118_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replica',
            name='candidates',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='replica',
            name='numimages',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='replica',
            name='numtasks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='replica',
            name='participants',
            field=models.IntegerField(default=0),
        ),
    ]