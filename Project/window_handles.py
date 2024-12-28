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
open_tab = driver.find_element(By.ID,"opentab")
open_tab.click()

windows = driver.window_handles
# for window in windows:
#     driver.switch_to.window(window)
#     if(driver.current_url.__contains__("qaclickacademy")):
#         print(driver.title)
print(driver.current_url)
driver.switch_to.window(windows[1])
print(driver.current_url)
