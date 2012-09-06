
#!/bin/sh

# This script takes the name of a server and the public key and connects then runs the commands to install puppet and git
# then it does a git clone of our config
# and a puppet apply to get jetty installed

EC2HOST=$1

KEYFILE=$2

ssh -i $KEYFILE ec2-user@$EC2HOST 'sudo yum -y install puppet git'
ssh -i $KEYFILE ec2-user@$EC2HOST 'git clone https://github.com/simonvc/puppet-jetty.git'
ssh -i $KEYFILE ec2-user@$EC2HOST 'ls -ltr puppet-jetty'
ssh -i $KEYFILE ec2-user@$EC2HOST 'cd puppet-jetty && sudo puppet apply manifests/init.pp'




