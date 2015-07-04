# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20150704_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(default='product1', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quantity',
            name='model',
            field=models.ForeignKey(related_name='+', to='inventory.Product'),
            preserve_default=True,
        ),
    ]
