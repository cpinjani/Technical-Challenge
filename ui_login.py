"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Description: UI test for Login into Rancher
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Author: Chandan Pinjani
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import subprocess, time

class RancherLogin():

    def setUp(self):
        self.profile = webdriver.FirefoxProfile()
        self.profile.accept_untrusted_certs = True
        self.driver = webdriver.Firefox(firefox_profile=self.profile)

        #Performing Rancher single node docker install
        subprocess.call(["./install_rancher_ui.sh"])
        
        #Sleeping for container to come up
        time.sleep(60)
        
        #Get container id
        self.cid = subprocess.getoutput("sudo docker ps -aqf name=rancher_ui")
        assert self.cid != ""
        
        #Get login password
        self.pwd = subprocess.getoutput(f"sudo docker logs {self.cid} 2>&1 | grep -i 'Bootstrap Password:'")
        self.pwd = self.pwd.split(" ")[-1]
        return self.pwd
        
    def rancher_ui_test(self, ip, pwd):
        driver = self.driver
        driver.get(f"http://{ip}:80")
        
        # Test1 Login Rancher Web page
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div/input'))).send_keys(pwd)
        driver.find_element(By.ID, 'submit').click()
        
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/main/div/form/div/div[1]/div[2]/div[6]/div/label/span[1]'))).click()
        time.sleep(10) 
        driver.find_element(By.ID, 'submit').click()
        time.sleep(10)
        
        # Test2 Main web page
        WebDriverWait(driver, 5).until(EC.url_matches(f"https://{ip}/dashboard/home"))
        
        # Test3 Main web page title is correct
        WebDriverWait(driver, 5).until(EC.title_is("Rancher"))


    def tearDown(self):
        self.driver.close()


run = RancherLogin()
pwd = run.setUp()
run.rancher_ui_test("127.0.0.1", pwd)
run.tearDown()
