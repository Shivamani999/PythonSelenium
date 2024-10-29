from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

#print(driver.get_screenshot_as_base64())
#driver.get_screenshot_as_file("ss.png")
print(driver.get_screenshot_as_png())