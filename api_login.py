"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Description: API test for Login into Rancher
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Author: Chandan Pinjani
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import requests
import subprocess, time

#Performing Rancher single node docker install
subprocess.call(["./install_rancher_api.sh"])

#Sleeping for container to come up
time.sleep(60)

#Get container id
cid = subprocess.getoutput("sudo docker ps -aqf name=rancher")
assert cid != ""

#Get login password
pwd = subprocess.getoutput(f"sudo docker logs {cid} 2>&1 | grep -i 'Bootstrap Password:'")
pwd = pwd.split(" ")[-1]

req_data = {"username": "admin", "password": pwd, "responseType":"cookie"}

#Login function
def login(ip, data):
        response = requests.post(f"https://{ip}/v3-public/localProviders/local?action=login",
            json=data, verify=False)
        result = response.status_code
        print(f"Status code: {result}")
        assert result == 200, "Login failed!"
        return result


try:
    login("127.0.0.1", req_data)
    print("Login success!")
except AssertionError as msg:
    print(msg)
