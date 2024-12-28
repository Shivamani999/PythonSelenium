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
frame = driver.find_element(By.ID,"courses-iframe")
driver.switch_to.frame(frame)
ele = driver.find_element(By.XPATH,"//div[@class='nav-outer clearfix']//a[text()='Courses']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
ele.click()
time.sleep(5)
driver.switch_to.parent_frame()
