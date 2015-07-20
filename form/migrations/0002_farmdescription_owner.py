# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmdescription',
            name='owner',
            field=models.CharField(verbose_name='Owner', max_length=100, default=''),
            preserve_default=True,
        ),
    ]
