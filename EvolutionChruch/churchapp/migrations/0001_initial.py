# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_fname', models.CharField(max_length=30)),
                ('person_lname', models.CharField(max_length=30)),
                ('person_birthday', models.DateTimeField(default=django.utils.timezone.now)),
                ('person_email', models.CharField(max_length=100)),
                ('person_maritalstatus', models.CharField(max_length=2)),
            ],
        ),
    ]
