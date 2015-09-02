# ScaleIO
Our first Ansible playbook installing MDM/SDS part of a ScaleIO setup
Vagrant file included to play around with it.

First Install virtualbox and Vagrant.
After installing both packages, issue a "vagrant up" and 3 centos hosts will be installed.
Then install Vagrant (we used Brewster for it, the missing package manager for OSX.)

Now you can setup the whole ScaleIO environment using "ansible-playbook scalio.yml".
Sit back and relax and let cowsay tell you which tasks are being run.

Next step is to configure storage from the SDS hosts and create volumes

