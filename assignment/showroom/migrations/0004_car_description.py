# Generated by Django 5.0 on 2023-12-24 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0003_car_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]