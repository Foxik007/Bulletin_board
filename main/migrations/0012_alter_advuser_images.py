# Generated by Django 4.0.6 on 2022-08-07 19:28

from django.db import migrations, models
import main.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_advuser_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advuser',
            name='images',
            field=models.ImageField(blank=True, upload_to=main.utilities.get_timestamp_path, verbose_name='Аватарка'),
        ),
    ]