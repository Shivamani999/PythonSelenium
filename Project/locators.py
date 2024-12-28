import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.find_element(By.NAME, "name").send_keys("Shivamani")
# driver.find_element(By.NAME, "email").send_keys("shivasuriyakonam@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "input#exampleInputPassword1").send_keys("Shivasuriya@99")
# driver.find_element(By.ID, "exampleCheck1").click()
# driver.find_element(By.XPATH, "//input[@type='submit']").click()
# msg = driver.find_element(By.CLASS_NAME, "alert-success").text
# print(msg)
# assert "Success123" in msg

# Xpath = //tagname[@attribute='value']
# CSS = tagname[attribute='value']
#       tagname#id or tagname.

driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input#userPassword").send_keys("123456")
driver.find_element(By.ID, "confirmPassword").send_keys("123456")
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
time.sleep(2)