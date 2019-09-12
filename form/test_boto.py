import boto
import os
import sys

def main():
  # this should come from Django later
  ec2_access_key = 'svallero'
  ec2_secret_key = '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'
  #ec2_access_key = 'oneadmin'
  #ec2_secret_key = 'd2154097e7420fb39d8b101dd521cc29717772eb'
  ssh_key = 'sara'
  master_image = 'ami-00000984'
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
 
  try:
    import logging
    logging.getLogger('boto').setLevel(logging.DEBUG)
    logging.getLogger('urllib3').setLevel(logging.DEBUG)
    boto.set_file_logger('boto', 'boto.log')
    conn=boto.connect_ec2_endpoint("https://one-master.to.infn.it/ec2api",
                                 aws_access_key_id=str(ec2_access_key),
                                 aws_secret_access_key=str(ec2_secret_key),
				 #validate_certs=False,
				 is_secure=True,
                                 debug=10)
#    conn.run_instances(master_image,instance_type=master_flavour,key_name=ssh_key)
    print (conn.get_params())
    #conn.run_instances(master_image,instance_type=master_flavour)
    conn.get_all_reservations()
    #print ("Error: ",conn.ResponseError)
    #reservations = conn.get_all_reservations(dry_run = True)
    #reservations = conn.get_only_instances()
#    inst=reservations[0].instances
    #return inst[-1]
    #print inst 
#    print (boto.exception.EC2ResponseError)
    #return 1
  except:
     print ("Ciccia!") 
     errore = sys.exc_info()[0]
     print( "<p>Error: %s</p>" % errore )
     raise
  #except Exception as e:
    #print(e) 

main()
  

