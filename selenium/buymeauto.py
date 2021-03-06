import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from getpass import getpass

name = input("Enter your name: ")
email = input("Enter your email: ")
password = getpass("Enter your password: ")

delay = 5

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"

driver = webdriver.Chrome(executable_path="chromedriver.exe", desired_capabilities=capa)
wait = WebDriverWait(driver, delay)
driver.get("https://buyme.co.il/")


#  function that enter into login / registration
def entry_button():
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="ember591"]/div/ul[1]/li[3]/a/span[2]').click()


# function that create account
def create_account():
    entry_button()
    driver.find_element_by_xpath('//*[@id="ember572"]/div/div[1]/div/div/div[3]/p/span').click() # click on the button to go to registerion
    driver.find_element_by_xpath("//input[@type='text']").send_keys(name) # set name into information register
    driver.find_element_by_xpath("//input[@type='email']").send_keys(email) # set email into information register
    password = driver.find_element_by_xpath('//*[@id="valPass"]').send_keys(password) # set password into information register
    ConfirmPassword = driver.find_element_by_xpath('//*[@id="ember1033"]').send_keys(password) # set confirm password into information register
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//*[@id="ember1034"]/label/i')) # click on check box that we agree to the terms
    driver.find_element_by_xpath('//*[@id="ember1025"]/button').click() # click on the button to register


# function that login with create account that we create
def login():
    entry_button()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@type='email']").send_keys(email)
    driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
    driver.find_element_by_xpath('//*[@id="ember1005"]/button').click()


# function that push information search
def which_gift():
    login()
    time.sleep(1)
    # sum of money
    driver.find_element_by_partial_link_text(r"סכום").click()
    driver.find_element_by_xpath('//*[@id="ember664_chosen"]/div/ul/li[2]').click()
    # area
    driver.find_element_by_partial_link_text(r"אזור").click()
    driver.find_element_by_xpath('//*[@id="ember679_chosen"]/div/ul/li[3]').click()
    # category
    driver.find_element_by_partial_link_text(r"קטגוריה").click()
    driver.find_element_by_xpath('//*[@id="ember689_chosen"]/div/ul/li[7]').click()
    # find me gift
    driver.find_element_by_id('ember724').click()


# This function enters the card and puts in the money we want to charge the card
def business_screen():
    which_gift()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ember1177"]/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ember572"]/div/div[2]/div[2]/div/div[2]/a[4]/span').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ember1276"]').send_keys("200")
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ember1275"]/div[2]/div/button').click()


# This function pushes the user's information into the purchase
def sender_receiver():
    business_screen()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ember1317"]/label[2]/span[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ember1317"]/label[1]/span[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ember1809"]').send_keys("זוהר")
    driver.find_element_by_xpath('//*[@id="ember1811"]').clear()
    driver.find_element_by_xpath('//*[@id="ember1811"]').send_keys("עמית")
    driver.find_element_by_xpath('//*[@id="ember1813_chosen"]/a/span').click()
    driver.find_element_by_xpath('//*[@id="ember1813_chosen"]/div/ul/li[4]').click()
    photo = driver.find_element_by_xpath('//*[@id="ember1815"]')
    photo.send_keys(r'C:\Users\97250\Desktop\selenium\img\img_01.JPG')
    time.sleep(15)
    driver.find_element_by_xpath('//*[@id="ember1310"]/div[3]/div/div[1]/label[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="ember1310"]/div[3]/div/div[1]/label[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="ember1310"]/div[4]/div/div[1]/div[2]/div/button/span/span[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//input[@type="email"]').send_keys(email)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ember1310"]/div[4]/div/div[3]/div/div[2]/button[2]').click()


def loading_screen():
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app-loading-img > div > div.bounce1')))
        driver.execute_script("window.stop();")
        print(driver.find_element_by_xpath('//*[@id="app-loading-img"]/div').size)
        print(driver.find_element_by_xpath('//*[@id="app-loading-img"]/div/div[1]').size)
        driver.quit()
    except ValueError as err:
        print('the site is not good ' + str(err))
    finally:
        driver.quit()
