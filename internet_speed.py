from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os
from time import sleep
from dotenv import load_dotenv
import secrets
load_dotenv()
EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
UPPER_LIMIT = 15
LOWER_LIMIT = 2
URL = 'https://www.speedtest.net/'
SERVICE = Service("C:\good_development\chromedriver.exe")


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=SERVICE)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url=URL)
        sleep(15)
        cancel = self.driver.find_element(By.CLASS_NAME, 'onetrust-close-btn-handler')
        cancel.click()
        sleep(5)
        start = self.driver.find_element(By.CLASS_NAME, 'js-start-test')
        start.click()
        sleep(185)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        pass

    def tweet_provider(self):
        self.driver.get(url='https://www.twitter.com')
        sleep(10)
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in.click()
        sleep(7)
        # base_window = self.driver.window_handles[0]
        # print(base_window)
        # new_login_window = self.driver.window_handles[1]
        # self.driver.switch_to.window(new_login_window)
        input_email = self.driver.find_element(By.NAME, "text")
        print(EMAIL)
        input_email.send_keys(EMAIL)
        input_email.send_keys(Keys.ENTER)
        sleep(5)

        sleep(4)
        username = self.driver.find_element(By.NAME, 'text')
        username.send_keys('codex_michael')
        username.send_keys(Keys.ENTER)

        sleep(3)

        input_pass = self.driver.find_element(By.NAME, 'password')
        input_pass.send_keys(PASSWORD)
        input_pass.send_keys(Keys.ENTER)
        sleep(5)
        tweet_link = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_link.click()
        sleep(4)
        tweet = f"my current internet download speed is {self.down}"
        tweet_text = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        tweet_text.send_keys(tweet)
        sleep(3)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div')
        tweet_button.click()

print(secrets.token_hex(23))
print(secrets.token_hex(23))