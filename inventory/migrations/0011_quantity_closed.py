# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_quantity_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantity',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
