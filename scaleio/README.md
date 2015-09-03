# ScaleIO and Ansible
My first Ansible playbook installing MDM/SDS part of a ScaleIO setup.
Vagrant file included to play around with it.

First Install Virtualbox and Vagrant on your system.
After installing both packages, issue a "vagrant up" and 3 centos hosts will be installed.
Then install Ansible (used Brewster for it on my Mac, the missing package manager for OSX.)
And also down your free copy of ScaleIO on: http://www.emc.com/products-solutions/trial-software-download/scaleio.htm

Now setup the whole ScaleIO environment using "ansible-playbook scalio.yml".
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





