# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20150708_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmdescription',
            name='master_image',
            field=models.CharField(max_length=30, default='CentOS', verbose_name='OS image', choices=[('ami-00000663', '663 - UbuntuServer 14.04'), ('ami-00000653', '653 - CentOS 6.6')]),
        ),
    ]
