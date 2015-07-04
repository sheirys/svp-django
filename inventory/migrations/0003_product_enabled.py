# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_warehouse_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='enabled',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
