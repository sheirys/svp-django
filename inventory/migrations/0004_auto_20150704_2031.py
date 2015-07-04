# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_product_enabled'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('model', models.ForeignKey(related_name='model', to='inventory.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='total_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='model',
        ),
    ]
