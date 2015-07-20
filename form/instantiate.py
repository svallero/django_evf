import boto
from django.conf import settings 
from form.models import FarmDescription
from binascii import b2a_base64, b2a_uu
import os
from  base64 import b64encode
from textwrap import indent

#def main(access, secret, flavour,image):
def main(farm):
  retval='dummy'
  # get farm parameters
  ec2_access_key=farm.ec2_access_key
  ec2_secret_key=farm.ec2_secret_key
  ssh_key=farm.ssh_key
  master_image=farm.master_image
  master_flavour=farm.master_flavour
  master_userdata=farm.master_userdata 
  worker_flavour=farm.worker_flavour
  worker_userdata=farm.worker_userdata 
  shared_secret=farm.shared_secret
  check_queue_every=farm.check_queue_every
  min_job_waiting_time=farm.min_job_waiting_time
  jobs_per_vm=farm.jobs_per_vm
  check_vms_every=farm.check_vms_every
  kill_idle_after=farm.kill_idle_after
  min_num_workers=farm.min_num_workers
  max_num_workers=farm.max_num_workers
  vm_deploy_time=farm.vm_deploy_time
  #################################

  # substitute variables in slave template file
  try:
     f_slave=open('/Users/svallero/Django/evf_provisioning/evf/context_files/context_slave_centos.cloudinit','r')
     user_data_slave=f_slave.read()
     user_data_slave=user_data_slave.replace("<condor_secret>", str(shared_secret))
     user_data_slave=user_data_slave.replace("<worker_userdata>", indent(worker_userdata,'     '))
     # encode workers user-data in base64 
     user_data_slave_b64=b64encode(user_data_slave.encode('utf-8')).decode('ascii')
  except:
     retval='ERROR - could not open and edit slave template file!' 
     return retval
  
  # substitute variables in master template file
  try:
     f_master=open('/Users/svallero/Django/evf_provisioning/evf/context_files/context_master_centos.cloudinit','r')
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
     user_data_master=user_data_master.replace("<master_userdata>", indent(master_userdata,'     '))
  except:
     retval='ERROR - could not open and edit master template file!' 
     return retval


  # make ec2 connection and run instance
  try:
     conn=boto.connect_ec2_endpoint("https://one-master.to.infn.it/ec2api/",
                                 aws_access_key_id=ec2_access_key,
                                 aws_secret_access_key=ec2_secret_key,
                                 validate_certs=False)
     conn.run_instances(master_image,instance_type=master_flavour,key_name=ssh_key, user_data=str(user_data_master))
     reservations = conn.get_all_reservations()
     inst=reservations[0].instances
  except:
     retval='ERROR - could not make ec2 connection and run instance!' 
     return retval

  return inst[-1]

