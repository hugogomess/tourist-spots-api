# Generated by Django 2.2.4 on 2019-08-11 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_one', models.CharField(max_length=150)),
                ('line_two', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
    ]
