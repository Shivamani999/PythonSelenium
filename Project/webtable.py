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
webtable = driver.find_element(By.XPATH,"//table[@id='product']/tbody")
driver.execute_script("arguments[0].scrollIntoView();",webtable)
rows = webtable.find_elements(By.TAG_NAME,"tr")
for row in rows:
    cols = row.find_elements(By.TAG_NAME,"td")
    for col in cols:
        if(col.text.__contains__("Selenium")):
            print(col.text)