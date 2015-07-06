# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20150706_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 20, 52, 59, 468730, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
