# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-09 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flyme', '0005_auto_20170625_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordsWall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.TextField(max_length=100, verbose_name='\u7559\u8a00')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('recall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='flyme.Recall')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
