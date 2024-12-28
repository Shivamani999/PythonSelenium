from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("headless")
chrome_opt.add_argument("--ignore-certificate-errors")

def setup_driver():
    ser_obj = Service("D:\chromedriver.exe")
    driver = webdriver.Chrome(service=ser_obj, options=chrome_opt)
    return driver

driver = setup_driver()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# driver.execute_script("window.scrollBy(0, 500);")
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
driver.get_screenshot_as_file("ss.png")
# driver.get_screenshot_as_png()
