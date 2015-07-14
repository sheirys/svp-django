# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_quantity_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='accounting',
            field=models.IntegerField(choices=[(1, 'FIFO'), (2, 'FILO')], default=1),
        ),
    ]
