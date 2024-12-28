import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("--start-maximized")
chrome_opt.add_argument("--ignore-certificate-errors")

service = Service("D:/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_opt)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//a[text()='Shop']").click()
items = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for item in items:
    if item.find_element(By.XPATH, "div/h4/a").text.__contains__("iphone"):
        item.find_element(By.XPATH, "div/button").click()
        break

driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]").click()
driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='India']")))
driver.find_element(By.XPATH, "//a[text()='India']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
message = driver.find_element(By.XPATH, "//strong[text()='Success!']").text
assert message.__contains__("Success")
