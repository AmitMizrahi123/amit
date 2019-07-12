# setting up chrome browser on a desired page
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
# opening chrome browser on a desired page
driver.get("http://www.walla.co.il")
# Getting browser current page URL
print("url: "+driver.current_url)
# Getting browser current page title
print("title: "+driver.title)
# Getting browser current tab handle
print("handle: "+driver.current_window_handle)
# Getting browser first tab handle
print("handles: "+driver.window_handles[0])
# Getting current page source
print("source: "+driver.page_source)
# Closing current tab
driver.close()
# Closing driver session
driver.quit()
# Refreshing current page
driver.refresh()
# Navigating to previous page
driver.back()
# Navigating to next page
driver.forward()
############### ELEMENTS METHODS################
# Finding elements
driver.find_element_by_name("q")
driver.find_element(By.ID,value="q")
# Clicking an element
driver.find_element_by_id("firstButton").click()
# Submitting a form using an element
driver.find_element_by_id("submitButton").submit()
# Sending keys to an element
driver.find_element_by_id("textField").send_keys("hello")
# Sending keyboard keys to an element
driver.find_element(By.ID,value="123").send_keys(Keys.ENTER)
# Clearing an element
driver.find_element_by_id("textField").clear()
############### ELEMENTS INFORMATION ################
# Checking if element is displayed
driver.find_element_by_id("element").is_displayed()
# Checking if element is enabled
driver.find_element_by_id("element").is_enabled()
# Checking if element is selected
driver.find_element_by_id("element").is_selected()
# Getting an element text
print(driver.find_element_by_id("element").text)
# Getting an element attribute
print(driver.find_element_by_id("element").get_attribute("value"))
############### WAITS ################
# Waiting for X amount of seconds
time.sleep(1)
# Waiting up to a certain amount of seconds to find element/s
driver.implicitly_wait(10)
