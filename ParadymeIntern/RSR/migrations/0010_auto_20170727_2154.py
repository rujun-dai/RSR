# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-27 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0009_auto_20170726_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='skill',
            field=models.ManyToManyField(through='RSR.PersonToSkills', to='RSR.Person'),
        ),
        migrations.AlterField(
            model_name='persontocompany',
            name='EndDate',
            field=models.DateField(default=27, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='persontocompany',
            name='StartDate',
            field=models.DateField(default=27, verbose_name='Start Date'),
        ),
    ]
