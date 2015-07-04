# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20150704_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
