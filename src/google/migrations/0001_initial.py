# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Google',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'db_table': 'google',
                'managed': True,
            },
        ),
    ]
