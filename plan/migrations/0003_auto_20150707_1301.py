# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'Open'), (2, b'In progress'), (3, b'Stoped'), (4, b'Testing'), (5, b'Closed')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
