import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

PROMISED_UP = 100
PROMISED_DOWN = 100
X_USERNAME = "ezsggs"
X_PASSWORD = ""

SPEEDTEST_SITE = "https://www.speedtest.net/"
X_SITE = "https://x.com/home"

class InternetSpeedTwitterBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = ""
        self.down = ""

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_SITE)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        go_button.click()
        time.sleep(45)

        # try:
        #     close_button = self.driver.find_element(By.CSS_SELECTOR, ".close-btn")
        #     close_button.click()
        # except NoSuchElementException:
        #     pass

        download_speed = self.driver.find_element(By.CSS_SELECTOR, ".download-speed")
        upload_speed = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed")

        self.up = upload_speed.text
        self.down = download_speed.text

        print(download_speed.text, upload_speed.text)


    def tweet_at_provider(self):
        self.driver.get(X_SITE)
        time.sleep(5)

        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
                                         value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH,
                                            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(X_USERNAME)
        password.send_keys(X_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()

obj = InternetSpeedTwitterBot()
obj.get_internet_speed()
obj.tweet_at_provider()