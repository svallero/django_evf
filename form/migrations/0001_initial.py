# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmDescription',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('farm_name', models.CharField(default='', verbose_name='Farm name', max_length=100)),
                ('farm_description', models.TextField(default='', verbose_name='Farm description', max_length=1000)),
                ('ec2_access_key', models.CharField(default='', verbose_name='EC2 access key', max_length=100)),
                ('ec2_secret_key', models.CharField(default='', verbose_name='EC2 secret key', max_length=100)),
                ('ssh_key', models.CharField(default='', verbose_name='root ssh key', max_length=1000)),
                ('master_image', models.CharField(default='CentOS', choices=[('ami-00000380', 'UbuntuServer 14.04'), ('ami-00000560', 'CentOS 6.6')], verbose_name='Master image', max_length=30)),
                ('master_flavour', models.CharField(default='m1.small', choices=[('m1.tiny', 'm1.tiny'), ('m1.small', 'm1.small'), ('m1.medium', 'm1.medium'), ('m1.large', 'm1.large'), ('m1.xlarge', 'm1.xlarge')], verbose_name='Master flavour', max_length=30)),
                ('master_userdata', models.TextField(default='', verbose_name='Master user-data', max_length=1000)),
                ('worker_image', models.CharField(default='CentOS', choices=[('ami-00000380', 'UbuntuServer 14.04'), ('ami-00000560', 'CentOS 6.6')], verbose_name='Worker image', max_length=30)),
                ('worker_flavour', models.CharField(default='m1.small', choices=[('m1.tiny', 'm1.tiny'), ('m1.small', 'm1.small'), ('m1.medium', 'm1.medium'), ('m1.large', 'm1.large'), ('m1.xlarge', 'm1.xlarge')], verbose_name='Worker flavour', max_length=30)),
                ('worker_userdata', models.TextField(default='', verbose_name='Worker user-data', max_length=1000)),
                ('shared_secret', models.CharField(default='', verbose_name='Condor shared secret', max_length=100)),
                ('check_queue_every', models.CharField(default='15', verbose_name='Queue polling time (s)', max_length=100)),
                ('min_job_waiting_time', models.CharField(default='100', verbose_name='Minimum jobs waiting time (s)', max_length=100)),
                ('jobs_per_vm', models.CharField(default='6', verbose_name='Number of jobs per VM', max_length=100)),
                ('check_vms_every', models.CharField(default='45', verbose_name='VMs polling time (s)', max_length=100)),
                ('kill_idle_after', models.CharField(default='3600', verbose_name='Maximum VM idle time (s)', max_length=100)),
                ('min_num_workers', models.CharField(default='2', verbose_name='Min number of workers', max_length=100)),
                ('max_num_workers', models.CharField(default='10', verbose_name='Max number of workers', max_length=100)),
                ('vm_deploy_time', models.CharField(default='350', verbose_name='VM deploy time (s)', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
