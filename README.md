# Technical-Challenge
Tests are intended to run on Centos 7 version having graphical GUI. \

Please check executable permissions of shell files before running tests (create_gcp_vm.sh, install_rancher_api.sh, install_rancher_ui.sh) \
Ref command: \
$ sudo chmod +x script.sh 

---PREREQUISITES---

Level 1. 
- Install python3, selenium, geckodriver \
Ref commands: \
$ sudo yum install -y python3 firefox Xvfb \
$ sudo pip3 install requests selenium \
$ wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz \
$ tar -xf geckodriver-v0.26.0-linux64.tar.gz \
$ sudo chmod +x geckodriver \
$ sudo mv geckodriver /usr/local/bin/ \
$ sudo reboot 

Run test: \
$ python3 ui_login.py 

---------------------------------------------------------

Level 2.
- Remove the existing container rancher_ui before running level 2 test (since it uses the same ports) 
- Install python3 and requests module \
Ref commands: \
$ sudo pip3 install requests \
$ sudo docker ps \
$ sudo docker stop <container_id> \
$ sudo docker rm <container_id> 

Run test: \
$ python3 api_login.py

---------------------------------------------------------
Level 3.
- gcloud cli installed and login to gcloud performed. 

Run test: \
$ sh create_gcp_vm.sh 
