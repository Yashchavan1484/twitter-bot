from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
TWITTER_EMAIL = "yashchavan1357@gmail.com"
TWITTER_PASSWORD = "Epun47czdg"
TWITTER_USERNAME = "1456Xyz75223"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        cookie_button = self.driver.find_element(By.ID,"onetrust-accept-btn-handler")
        cookie_button.click()
        start_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_button.click()
        time.sleep(60)

        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(f"Download speed: {self.down} Mbps")
        print(f"Upload speed: {self.up} Mbps")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(4)

        #it will enter username directly
        username_login_button = self.driver.find_element(By.NAME,'text')
        username_login_button.send_keys(TWITTER_USERNAME)
        username_login_button.send_keys(Keys.ENTER)
        time.sleep(4)

        password_login_button = self.driver.find_element(By.NAME,"password")
        password_login_button.send_keys(TWITTER_PASSWORD)
        password_login_button.send_keys(Keys.ENTER)
        time.sleep(10)

        tweet_box = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey @InternetProvider, my internet speed is {self.down} download/{self.up} upload"
        tweet_box.send_keys(tweet)

        tweet_button = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        tweet_button.click()

        print("Tweet sent!")

        time.sleep(5)
        self.driver.quit()


