from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Variables where we will save our information about creating a user in the Instagram
email = input('insert email address: ')
fullName = input('insert full name address: ')
username = input('choose username: ')
password = input('insert password: ')

# A variable that we'll apply when we want to make a new user
user_exists = input('do you already have user in Instagram Y(Yes)/N(No): ').capitalize()

# A variable in which we know whether you are already following it or not
followOrNotFollow = input('do you already follow this user Y(Yes)/N(No): ').capitalize()

# A variable that let us know who you want to follow and give him likes
usernameLike = input('Enter the name of the user you want to follow and let him likes: ')


class Instagram:
    def __init__(self, email, fullName, username, password):
        self.email = email
        self.fullName = fullName
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome('chromedriver.exe')
        self.bot.maximize_window()

    def create_bot_user(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(3)
        email = bot.find_element_by_name('emailOrPhone')
        fullName = bot.find_element_by_name('fullName')
        userName = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        fullName.clear()
        userName.clear()
        password.clear()
        email.send_keys(self.email)
        fullName.send_keys(self.fullName)
        userName.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

    def login_bot_user(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(2)
        userName = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        userName.clear()
        password.clear()
        userName.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def choose_account(self, name, follow):
        bot = self.bot
        bot.get('https://www.instagram.com/' + name)
        time.sleep(3)
        if follow == 1:
            follow = bot.find_element_by_class_name('_0mzm-')
            follow.click()
        bot.execute_script('window.scrollBy(0, document.body.scrollHeight)')
        time.sleep(2)
        posts = bot.find_elements_by_class_name('v1Nh3')
        links = [elem.find_element_by_tag_name('a').get_attribute('href') for elem in posts]
        for link in links:
            bot.get(link)
            like_photo = bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button/span')
            like_photo.click()
            time.sleep(5)
        bot.quit()


if __name__ == '__main__':
    instabot = Instagram(email, fullName, username, password)
    while True:
        # check if user exists - Yes
        if user_exists == 'Y':
            # log in into your user
            instabot.login_bot_user()
            # check if you are following after your friend - Yes
            if followOrNotFollow == 'Y':
                # push data for instance function that overflow to add followers
                instabot.choose_account(usernameLike, 0)
            # check if you are following after your friend - Yes
            else:
                # push data for instance function to add followers 
                instabot.choose_account(usernameLike, 1)
            break
        # check if user exists - No
        else:
            # create your user
            instabot.create_bot_user()
            # log in into your user
            instabot.login_bot_user()
            # If you do not have a user then you probably are not following him so add him to your followers
            instabot.choose_account(usernameLike, 1)
            break
