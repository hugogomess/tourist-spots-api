# Generated by Django 2.2.4 on 2019-08-11 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attraction',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='opening_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
