Ok so the test is basically write a script that launches n instances and installs jetty. Which is easy. But the test mentions the following:

This file comes from https://github.com/simonvc/example_code_for_a_technical_test 

* Use an amazon linux AMI
* Use any tools resources etc 
* Production quality

Right, so a production quality solution would be.

* All code is stored in GIT (check)
* Use boto to spawn the VMs (check)
* Boto to create a keypair (check)
* Use SSH to install puppet via YUM (centos) or apt-get (debian) (check)
* Puppet manifests are stored in GIT (like all config should be) (check)
* Puppet to install Jetty (check)
