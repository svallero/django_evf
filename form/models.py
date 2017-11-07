from django.db import models
from django.core.urlresolvers import reverse



class FarmDescription(models.Model):

    IMAGES = (
        ('ami-00000679', '679 - UbuntuServer 14.04'),
        ('ami-00000687', '687 - CentOS 6.6'),
    )

    FLAVOURS = (
        ('m1.tiny', 'm1.tiny'),
        ('m1.small', 'm1.small'),
        ('m1.medium', 'm1.medium'),
        ('m1.large', 'm1.large'),
        ('m1.xlarge', 'm1.xlarge'),
    )

    # the farm object should belong to the logged user
    #owner=models.OneToOneField(User, primary_key=True,default='')
    #owner=models.ForeignKey(User, default='')
    owner=models.CharField(verbose_name='Owner', max_length=100, default='')
    farm_name = models.CharField(verbose_name="Farm name", max_length=100, default='')
    farm_description = models.TextField(verbose_name="Farm description", max_length=1000, default='')
    # cloud credentials
    ec2_access_key = models.CharField(verbose_name="EC2 access key", max_length=100, default='')
    ec2_secret_key = models.CharField(verbose_name="EC2 secret key", max_length=100, default='')
    # ssh key for root
    ssh_key = models.CharField(verbose_name="root ssh key", max_length=1000, default='')
    # master configuration
    master_image = models.CharField(verbose_name="OS image", max_length=30, choices=IMAGES, default='CentOS')
    master_flavour = models.CharField(verbose_name="Master flavour", max_length=30, choices=FLAVOURS, default='m1.small')
    #master_userdata = models.TextField(verbose_name="Master user-data", max_length=1000, default='')
    master_userdata = models.TextField(verbose_name="Master user-data", default='')
    # workers configuration
    #worker_image = models.CharField(verbose_name="Worker image", max_length=30, choices=IMAGES, default='CentOS')
    worker_flavour = models.CharField(verbose_name="Worker flavour", max_length=30, choices=FLAVOURS, default='m1.small')
    #worker_userdata = models.TextField(verbose_name="Worker user-data", max_length=1000, default='')
    worker_userdata = models.TextField(verbose_name="Worker user-data", default='')
    # condor shared secret
    shared_secret = models.CharField(verbose_name="Condor shared secret", max_length=100, default='')
    # elastiq configuration
    check_queue_every = models.CharField(verbose_name="Queue polling time (s)", max_length=100, default='15')
    min_job_waiting_time = models.CharField(verbose_name="Minimum jobs waiting time (s)", max_length=100, default='100')
    jobs_per_vm = models.CharField(verbose_name="Number of jobs per VM", max_length=100, default='6')
    check_vms_every = models.CharField(verbose_name="VMs polling time (s)", max_length=100, default='45')
    kill_idle_after = models.CharField(verbose_name="Maximum VM idle time (s)", max_length=100, default='3600')
    min_num_workers = models.CharField(verbose_name="Min number of workers", max_length=100, default='2')
    max_num_workers = models.CharField(verbose_name="Max number of workers", max_length=100, default='10')
    vm_deploy_time = models.CharField(verbose_name="VM deploy time (s)", max_length=100, default='350')

    def get_absolute_url(self):
        return reverse('form:display_farm', kwargs={'pk': self.pk})


    def form_valid(self, form):
        return super(FarmDescription, self).form_valid(form)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in FarmDescription._meta.fields]

    def __str__(self):              # __unicode__ on Python 2
     return self.farm_name



