# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-31 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('published', models.DateTimeField()),
                ('image', models.ImageField(upload_to='media/')),
                ('body', models.TextField()),
            ],
        ),
    ]