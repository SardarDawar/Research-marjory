# Generated by Django 3.1.3 on 2020-11-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0014_auto_20201123_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='replica',
            name='save_uncompleted_scripts_email_contactme',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='replica',
            name='save_uncompleted_scripts',
            field=models.BooleanField(default=False),
        ),
    ]