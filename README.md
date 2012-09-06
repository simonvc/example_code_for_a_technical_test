Ok so the test is basically write a script that launches n instances and installs jetty. Which is easy. But the test mentions the following:

* Use an amazon linux AMI
* Use any tools resources etc 
* Production quality

Right, so a production quality solution would be.

* All code is stored in GIT (check)
* Use boto to spawn the VMs
* Boto to create a keypair
* Use SSH to install puppet via YUM (centos) or apt-get (debian)
* Puppet manifests are stored in GIT (like all config should be)
* Puppet to install Jetty
