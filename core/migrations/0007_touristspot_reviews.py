# Generated by Django 2.2.4 on 2019-08-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20190811_0828'),
        ('core', '0006_touristspot_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='reviews',
            field=models.ManyToManyField(to='reviews.Review'),
        ),
    ]