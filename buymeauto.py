from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://buyme.co.il/")


#  function that enter into login / registration
def entry_button():
    for entryButton in driver.find_elements_by_xpath(r'//*[@id="ember591"]/div/ul[1]/li[3]/a/span[2]'):
        entryButton.click()


# function that create account
def create_account():
    entry_button()
    for entryLogin in driver.find_elements_by_xpath(r'//*[@id="ember572"]/div/div[1]/div/div/div[3]/p/span'):
        entryLogin.click()
    driver.find_element_by_xpath("//input[@type='text']").send_keys("amit")
    driver.find_element_by_xpath("//input[@type='email']").send_keys("amitmizrahi231055@gmail.com")
    for password in driver.find_elements_by_xpath("//input[@type='password']"):
        password.send_keys("MF4ever!")
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//*[@id="ember1034"]/label/i'))
    driver.find_element_by_xpath('//*[@id="ember1025"]/button').click()


# function that login with create account that we create
def login():
    entry_button()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@type='email']").send_keys("amitmizrahi231055@gmail.com")
    driver.find_element_by_xpath("//input[@type='password']").send_keys("MF4ever!")
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
    driver.find_element_by_xpath('//input[@type="email"]').send_keys("amitmizrahi231055@gmail.com")
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ember1310"]/div[4]/div/div[3]/div/div[2]/button[2]').click()
