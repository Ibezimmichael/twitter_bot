from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
import time
import internet_speed
from dotenv import load_dotenv
load_dotenv()
EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
UPPER_LIMIT = 15
LOWER_LIMIT = 2
SERVICE = Service("C:\good_development\chromedriver.exe")

bot = internet_speed.InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_provider()

