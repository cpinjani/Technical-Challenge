#!/bin/bash

VM_NAME="my-suse-test"

echo "Creating VM in GCP, this might take a while.."
echo "----------------------------------------------"

# Using gcloud cli
result=$(gcloud compute instances create $VM_NAME --image-family=sles-15 --image-project=suse-cloud --zone=us-central1-a --network-interface=subnet=default 2>&1)

if [ $? -eq 0 ]
then 
  echo "Successfully created instance with name : $VM_NAME"
else 
  echo "Instance creation failed with error: $result"
fi
