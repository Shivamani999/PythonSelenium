from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
driver.implicitly_wait(10)

ele = driver.find_element(By.XPATH,"//span[text()='Courses']")
print(ele.is_displayed())
print(ele.is_enabled())
ele.screenshot("ele.png")
#ele.text