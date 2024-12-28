# Expected Conditions –
# There are some common conditions that are frequently of use when automating web browsers.

# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

service_obj = Service("D:/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
act_lst = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
ber_veggies = driver.find_elements(By.XPATH, "//div[@class='products']/div")
exp_lst = []

assert len(ber_veggies) > 0
for i in ber_veggies:
    exp_lst.append(i.find_element(By.XPATH, "h4").text)
    i.find_element(By.XPATH, "div/button").click()

assert act_lst == exp_lst

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
total_amount = 0
amounts = driver.find_elements(By.XPATH, "//table[@id='productCartTables']/tbody/tr/td[5]/p[@class='amount']")
for i in amounts:
    total_amount += int(i.text)
tot_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert total_amount == tot_amount

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
# time.sleep(5)
wait = WebDriverWait(driver, 10) # Explicit wait
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)
dis_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert tot_amount > dis_amount
