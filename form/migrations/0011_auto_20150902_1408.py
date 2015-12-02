# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0010_auto_20150722_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmdescription',
            name='master_userdata',
            field=models.TextField(verbose_name='Master user-data', default=''),
        ),
        migrations.AlterField(
            model_name='farmdescription',
            name='worker_userdata',
            field=models.TextField(verbose_name='Worker user-data', default=''),
        ),
    ]
