import boto
import paramiko # so i can use SSH to control the instances
from time import sleep

ec2 = boto.connect_ec2()


# Ami to lanunch 
AMI='ami-a0cd60c9' # A standard amazon ami
num_instances=1
keypair_name="simons_keypair_12"


# Ideally puppet and git should be packed into our personalized AMI but for now....
launch_data="""
#!/bin/bash
sudo yum install -y puppet git
"""
# 

def install_tools():
  pass

if '__main__' in __name__:
  print "Starting %s instances of %s" % (num_instances, AMI)

  key_pair = ec2.create_key_pair(keypair_name) 
  key_pair.save('/home/simonvc/.ssh')

  reservations=[]
  for n in range(num_instances):
    reservations.append( ec2.run_instances(image_id=AMI, key_name=keypair_name, instance_type='t1.micro', user_data=launch_data) )

  sleep(60) # This should be changed to a while loop that checks the number of instances in the colleciton or reservations todo:

  print reservations

  for r in reservations:
    print r
    print dir(r)
    print r.instances[0].public_dns_name
    for instance in r.instances:
      print instance
      print dir(instance) # cant remember how boto stores this data
      print instance.public_dns_name
      install_tools(instance.public_dns_name)

