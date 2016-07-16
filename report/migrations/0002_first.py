# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_0001_first'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Catagory', models.CharField(max_length=100)),
                ('report_location', models.CharField(max_length=100)),
                ('trafficker_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Catagory',
        ),
        migrations.DeleteModel(
            name='Issue_desc',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Trafficker_name',
        ),
    ]