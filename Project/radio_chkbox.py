import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

chkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for i in chkboxes:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected()
        break
time.sleep(2)

radiobtn = driver.find_elements(By.XPATH, "//input[@type='radio']")
# for i in radiobtn :
#     if i.get_attribute("value") == "radio3":
#         i.click()
#         assert i.is_selected()
#         break
radiobtn[2].click()
assert radiobtn[2].is_selected()
time.sleep(2)

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()
