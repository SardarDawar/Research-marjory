# Generated by Django 3.1.3 on 2020-12-01 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0009_script_script_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='comments',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
