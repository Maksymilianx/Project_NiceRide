# Generated by Django 3.2.3 on 2021-09-16 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NiceRide', '0004_alter_car_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand_of_car',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
