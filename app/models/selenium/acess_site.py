import glob
import os
import time
from app.config import DOWNLOAD_FILE
from app.models.selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class getCsvFile:
    
    def __init__(self, driver, url, login, pwd):
        self.driver = driver
        self.url = url
        self.login = login
        self.pwd = pwd
        
    def site(self):
        self.driver = webdriver.Chrome(self.driver)
        self.driver.get(self.url)   
        
        a=1

    def login_site(self):
        self.driver.find_element_by_xpath("//div[@class='ipc-button__text'][normalize-space()='Fazer login']").click()
        self.driver.find_element_by_xpath("//span[normalize-space()='Sign in with IMDb']").click()
        self.driver.find_element_by_xpath("//input[@id='ap_email']").send_keys(self.login)
        self.driver.find_element_by_xpath("//input[@id='ap_password']").send_keys(self.pwd)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        a=1
    
    def clearFolder(self,folder):
        files = glob.glob(folder)
        for f in files:
            os.remove(f)    
        
    def download_favs(self):
        self.driver.find_element_by_xpath("//div[contains(text(),'Lista de favoritos')]").click()
        self.clearFolder(DOWNLOAD_FILE)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Export this list']").click()
        time.sleep(2)
        a=1
    