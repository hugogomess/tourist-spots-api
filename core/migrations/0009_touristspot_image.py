# Generated by Django 2.2.4 on 2019-08-12 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190811_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tourist_spot'),
        ),
    ]