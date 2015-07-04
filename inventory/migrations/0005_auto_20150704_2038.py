# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20150704_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantity',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quantity',
            name='warehouse',
            field=models.ForeignKey(default=1, to='inventory.Warehouse'),
            preserve_default=False,
        ),
    ]
