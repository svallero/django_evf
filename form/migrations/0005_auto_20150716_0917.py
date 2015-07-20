# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20150709_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmdescription',
            name='master_image',
            field=models.CharField(verbose_name='OS image', default='CentOS', choices=[('ami-00000663', '663 - UbuntuServer 14.04'), ('ami-00000674', '674 - CentOS 6.6')], max_length=30),
        ),
    ]
