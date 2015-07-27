# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0009_auto_20150721_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmdescription',
            name='master_image',
            field=models.CharField(verbose_name='OS image', choices=[('ami-00000679', '679 - UbuntuServer 14.04'), ('ami-00000687', '687 - CentOS 6.6')], max_length=30, default='CentOS'),
        ),
    ]
