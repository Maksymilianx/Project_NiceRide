# Generated by Django 3.2.3 on 2021-07-31 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NiceRide', '0003_auto_20210731_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
