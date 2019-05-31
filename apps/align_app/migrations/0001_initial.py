# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-05-28 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('sun_sign', models.CharField(max_length=45)),
                ('moon_sign', models.CharField(max_length=45)),
                ('rising_sign', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
