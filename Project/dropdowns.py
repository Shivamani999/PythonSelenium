import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

service_obj = Service("D:\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.implicitly_wait(5)
# select = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# select.select_by_index(1)
# time.sleep(2)
# select.select_by_visible_text("Male")
# time.sleep(2)

# driver.get("https://www.amazon.in/")
# driver.implicitly_wait(5)
# driver.find_element(By.ID, "twotabsearchtextbox").send_keys("apple")
# time.sleep(2)
# drpdwns = driver.find_elements(By.XPATH, "//div[@class='left-pane-results-container']/div")
# for i in drpdwns:
#     if "smart watch" in i.text:
#         i.click()
#         break
# time.sleep(2)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.implicitly_wait(5)
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
drpdwns = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
for i in drpdwns:
    if i.text == "India":
        i.click()
        break
time.sleep(2)
country = driver.find_element(By.ID, "autosuggest").get_attribute("value")
assert "India" == country