# Actions Class is called as Actions Chains

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

service_obj = Service("D:/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.amazon.in/")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

# visible_ele = driver.find_element(By.ID,"nav-link-accountList-nav-line-1")
# hide_ele = driver.find_element(By.XPATH,"//span[text()='Your Account']")

mouse = driver.find_element(By.ID, "mousehover")
reload = driver.find_element(By.XPATH, "//a[text()='Reload']")

actions = ActionChains(driver)
actions.move_to_element(mouse).perform()
actions.move_to_element(reload).click().perform()
# actions.send_keys("")
# actions.click_and_hold()
# actions.context_click()
# actions.double_click()
# actions.drag_and_drop()
# actions.key_up()
# actions.key_down()
# actions.scroll_to_element()
# actions.send_keys_to_element("")
