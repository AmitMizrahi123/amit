from selenium import webdriver
from getpass import getpass 

email = input("Enter your email: ")
password = getpass("Enter your password: ")

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.youtube.com/?hl=iw&tab=w1&gl=IL")


def login():
    driver.implicitly_wait(5)
    driver.find_element_by_partial_link_text('כניסה').click() # click on login button
    driver.find_element_by_id('identifierId').send_keys(email) # set email into information login
    driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click() # click to countinue
    driver.find_element_by_name('password').send_keys(password) # set password into information login
    driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click() # click to countinue


def print_mymix():
    login() # we need to login fisrt so first its go to login 
    driver.implicitly_wait(5)
    driver.fullscreen_window() # browser full screen
    driver.find_element_by_partial_link_text('עמית').click() # click on my mix
    print(driver.find_element_by_xpath('//*[@id="stats"]/yt-formatted-string[1]').text) # print out the number of songs in my mix
    for music in driver.find_elements_by_xpath('//*[@id="primary"]'):
        print(music.text) # loops over list of songs in my mix and print out the number song, how time the song go and the songer
    driver.quit()
