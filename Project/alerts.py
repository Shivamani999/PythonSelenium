import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def setup_driver():
    ser_obj = Service("D:\chromedriver.exe")
    driver = webdriver.Chrome(service=ser_obj)
    return driver

driver = setup_driver()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"alertbtn").click()
time.sleep(3)
alert = driver.switch_to.alert
alert.accept()
# alert.dismiss()
# alert.send_keys()
# alert.text