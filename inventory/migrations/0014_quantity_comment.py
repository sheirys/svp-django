# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20150714_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantity',
            name='comment',
            field=models.TextField(null=True, blank=True),
        ),
    ]
