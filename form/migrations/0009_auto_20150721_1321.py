# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_auto_20150717_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmdescription',
            name='master_image',
            field=models.CharField(choices=[('ami-00000679', '679 - UbuntuServer 14.04'), ('ami-00000686', '686 - CentOS 6.6')], max_length=30, verbose_name='OS image', default='CentOS'),
        ),
    ]
