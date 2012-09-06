Ok so the test is basically write a script that launches n instances and installs jetty. Which is easy. But the test mentions the following:

* Use an amazon linux AMI
* Use any tools resources etc 
* Production quality

Right, so a production quality solution would be.

1/ All code is stored in GIT (check)
2/ Use boto to spawn the VMs
3/ Boto to create a keypair
4/ Use SSH to install puppet via YUM (centos) or apt-get (debian)
5/ Puppet manifests are stored in GIT (like all config should be)
6/ Puppet to install Jetty
