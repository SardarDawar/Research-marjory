# Generated by Django 3.1.3 on 2020-12-01 17:41

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20201201_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='color_header_bg',
            field=colorfield.fields.ColorField(default='#417690', max_length=18),
        ),
        migrations.AddField(
            model_name='setting',
            name='color_header_font',
            field=colorfield.fields.ColorField(default='#FFD966', max_length=18, verbose_name='Header font color'),
        ),
        migrations.AddField(
            model_name='setting',
            name='color_nav_foot_bg',
            field=colorfield.fields.ColorField(default='#79AEC8', max_length=18),
        ),
        migrations.AddField(
            model_name='setting',
            name='color_nav_foot_font',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
    ]