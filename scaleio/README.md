# ScaleIO and Ansible
My first Ansible playbook installing MDM/SDS part of a ScaleIO setup.
Vagrant file included so you can quickly start to play with it.

First install Virtualbox and Vagrant on your system.
After installing both packages, issue a "vagrant up" and 3 centos hosts will be installed:
$ vagrant up
Bringing machine 'vagrant1' up with 'virtualbox' provider...
Bringing machine 'vagrant2' up with 'virtualbox' provider...
Bringing machine 'vagrant3' up with 'virtualbox' provider...

Then install Ansible (used Brewster for it on my Mac, the missing package manager for OSX.)
And also download your free copy of ScaleIO on: http://www.emc.com/products-solutions/trial-software-download/scaleio.htm and place el6 linux .rpm packages in files directory.

Now setup the ScaleIO environment using "$ ansible-playbook scaleio.yml".
Sit back and relax and let cowsay tell you which tasks are being run, moooe:
____________ 
< PLAY RECAP >
 ------------ 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||


scaleio01                  : ok=19   changed=10   unreachable=0    failed=0   
scaleio02                  : ok=8    changed=1    unreachable=0    failed=0   
scaleio03                  : ok=8    changed=1    unreachable=0    failed=0 




