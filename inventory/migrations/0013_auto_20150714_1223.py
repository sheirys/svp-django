# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20150707_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuantityProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='quantity',
            name='model',
        ),
        migrations.RemoveField(
            model_name='quantity',
            name='quantity',
        ),
        migrations.AddField(
            model_name='quantityproduct',
            name='code',
            field=models.ForeignKey(related_name='+', to='inventory.Quantity'),
        ),
        migrations.AddField(
            model_name='quantityproduct',
            name='model',
            field=models.ForeignKey(related_name='+', to='inventory.Product'),
        ),
    ]
