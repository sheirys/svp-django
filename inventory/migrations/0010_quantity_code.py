# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_product_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantity',
            name='code',
            field=models.CharField(default='code1', unique=True, max_length=50),
            preserve_default=False,
        ),
    ]
