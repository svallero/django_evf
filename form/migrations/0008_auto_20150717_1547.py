# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_auto_20150717_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmdescription',
            name='master_image',
            field=models.CharField(max_length=30, choices=[('ami-00000679', '679 - UbuntuServer 14.04'), ('ami-00000675', '675 - CentOS 6.6')], verbose_name='OS image', default='CentOS'),
        ),
    ]
