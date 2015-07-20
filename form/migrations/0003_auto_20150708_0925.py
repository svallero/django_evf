# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_farmdescription_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmdescription',
            name='worker_image',
        ),
        migrations.AlterField(
            model_name='farmdescription',
            name='master_image',
            field=models.CharField(choices=[('ami-00000380', '380 - UbuntuServer 14.04'), ('ami-00000653', '653 - CentOS 6.6')], max_length=30, verbose_name='OS image', default='CentOS'),
        ),
    ]
