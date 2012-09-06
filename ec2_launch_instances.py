import boto
import paramiko # so i can use SSH to control the instances
from time import sleep

ec2 = boto.connect_ec2()


# Ami to lanunch 
AMI='ami-a0cd60c9' # A standard amazon ami
num_instances=2
keypair_name="simons_keypair_9"



if '__main__' in __name__:
  print "Starting %s instances of %s" % (num_instances, AMI)

  key_pair = ec2.create_key_pair(keypair_name) 
  key_pair.save('/home/simonvc/.ssh')

  reservations=[]
  for n in range(num_instances):
    reservations.append( ec2.run_instances(image_id=AMI, key_name=keypair_name, instance_type='t1.micro') )

  sleep(60) # This should be changed to a while loop that checks the number of instances in the colleciton or reservations todo:

  for r in reservations:
    print r.instances[0].public_dns_name

