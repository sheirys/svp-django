# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(related_name='+', default=1, to='plan.Project'),
            preserve_default=False,
        ),
    ]
