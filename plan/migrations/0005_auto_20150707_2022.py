# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_auto_20150707_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, 'Open'), (2, 'In progress'), (3, 'Stoped'), (4, 'Testing'), (5, 'Closed')], default=1),
        ),
    ]
