#!/usr/bin/env python

'''
Reset Energy counter on Sonoff PowR2
 Franc Rodriguez - TECOB (2019)
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


user = 'XXXXX'
password = 'XXXXX'
IpSonoff = '10.82.0.88'

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get('http://'+user+':'+password+'@'+IpSonoff+'')

# Click Sensors Menu
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/ul/li[10]/a")))
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/ul/li[10]/a').click()

# Toggle Reset Energy
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/form[14]/div/div[2]/fieldset/div[16]/div[1]/label')))
driver.find_element_by_xpath('/html/body/div[2]/div[2]/form[14]/div/div[2]/fieldset/div[16]/div[1]/label').click()

# Click Save Button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/button[1]")))
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/button[1]').click()
time.sleep(2)
driver.switch_to.alert.accept()

driver.close()
