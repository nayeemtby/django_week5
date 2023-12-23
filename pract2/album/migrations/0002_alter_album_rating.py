# Generated by Django 5.0 on 2023-12-23 08:35

import album.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=3, validators=[album.models.validate_rating], verbose_name='Rating'),
        ),
    ]
