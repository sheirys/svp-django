# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 4, 20, 5, 13, 470359, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
