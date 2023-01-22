#!/bin/bash

sudo yum install -y yum-utils

# Adding Docker repo
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

echo "---------------------------------------------"
echo "Installing docker service"
sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y
sudo systemctl start docker

echo "---------------------------------------------"
echo "Performing Rancher single node docker install"
sudo docker run -d --name rancher_api --restart=unless-stopped -p 80:80 -p 443:443 --privileged rancher/rancher:stable
if [[ $? -eq 0 ]]; then
echo "Done single node install of Rancher for API"
else
echo "Rancher installation failed"
fi

