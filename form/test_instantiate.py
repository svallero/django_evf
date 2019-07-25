#!/usr/bin/python

import boto
#from django.conf import settings 
import os
from  base64 import b64encode, encodestring

#def main(access, secret, flavour,image):
def main():
  BASE_DIR="/home/evf/django_evf/"
  # this should come from Django later
  ec2_access_key = 'svallero'
  ec2_secret_key = '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'
  ssh_key = 'sara'
  master_image = 'ami-00000983'
  master_flavour = 'm1.small'
  master_userdata =  'echo "pippo" > /root/pippo.txt'
  worker_flavour  = 'm1.large'
  worker_userdata =  'echo "pippo" > /root/pippo.txt'
  shared_secret = 'pippo'
  check_queue_every = 15
  min_job_waiting_time = 100
  jobs_per_vm =  6
  check_vms_every =  45
  kill_idle_after =  3600
  min_num_workers = 2
  max_num_workers = 10
  vm_deploy_time = 350
  ###########################################################################
 

  # substitute variables in template file
  #f=open(os.path.join(settings.BASE_DIR, 'context_files/context_master.cloudinit'),'r')
  #f_slave=open('/Users/svallero/Django/evf_provisioning/evf/context_files/context_slave_centos.cloudinit','r')
  f_slave=open(os.path.join(BASE_DIR, 'context_files/context_slave_centos.cloudinit'),'r')
  user_data_slave=f_slave.read()
  user_data_slave=user_data_slave.replace("<condor_secret>", str(shared_secret))
  # encode workers user-data in base64 
  user_data_slave_b64=b64encode(user_data_slave)
  
  #f_master=open('/Users/svallero/Django/evf_provisioning/evf/context_files/context_master_centos.cloudinit','r')
  f_master=open(os.path.join(BASE_DIR, 'context_files/context_master_centos.cloudinit'),'r')
  user_data_master=f_master.read()
  
  user_data_master=user_data_master.replace("<check_queue_every_s>", str(check_queue_every))
  user_data_master=user_data_master.replace("<check_vms_every_s>", str(check_vms_every))
  user_data_master=user_data_master.replace("<check_vms_in_error_every_s>", str(check_vms_every))
  user_data_master=user_data_master.replace("<waiting_jobs_time_s>", str(min_job_waiting_time))
  user_data_master=user_data_master.replace("<n_jobs_per_vm>", str(jobs_per_vm))
  user_data_master=user_data_master.replace("<idle_for_time_s>", str(kill_idle_after))
  user_data_master=user_data_master.replace("<estimated_vm_deploy_time_s>", str(vm_deploy_time))
  user_data_master=user_data_master.replace("<min_vms>", str(min_num_workers))
  user_data_master=user_data_master.replace("<max_vms>", str(max_num_workers))
  user_data_master=user_data_master.replace("<aws_access_key_id>", str(ec2_access_key))
  user_data_master=user_data_master.replace("<aws_secret_access_key>", str(ec2_secret_key))
  user_data_master=user_data_master.replace("<image_id>", str(master_image))
  user_data_master=user_data_master.replace("<key_name>", str(ssh_key))
  user_data_master=user_data_master.replace("<flavour>", str(worker_flavour))
  user_data_master=user_data_master.replace("<user_data_b64>", str(user_data_slave_b64))
  user_data_master=user_data_master.replace("<condor_secret>", str(shared_secret))

  #print (user_data_master)
  #print user_data_slave_b64


  conn=boto.connect_ec2_endpoint("https://one-master.to.infn.it/ec2api/",
                                 aws_access_key_id=ec2_access_key,
                                 aws_secret_access_key=ec2_secret_key,
                                 validate_certs=False)
  conn.run_instances(master_image,instance_type=master_flavour,user_data=user_data_master)
  reservations = conn.get_all_reservations()
  inst=reservations[0].instances
  return inst[-1]
  #return 1

main()
  

