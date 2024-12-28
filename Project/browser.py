import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome()
# time.sleep(2)

service_obj = Service("D:\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.amazon.in/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)
