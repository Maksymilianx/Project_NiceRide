# Generated by Django 3.2.3 on 2021-07-31 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NiceRide', '0002_car_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.CreateModel(
            name='OfferImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('car', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='NiceRide.car')),
            ],
        ),
    ]