# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20150704_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='accounting',
            field=models.IntegerField(default=1, choices=[(1, b'FIFO'), (2, b'FILO')]),
            preserve_default=True,
        ),
    ]
