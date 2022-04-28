from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PROMISSED_UP = 30
PROMISSED_DOWN = 20
USERNAME = "Tony29743808"

TWITTER_LOG = "tonyuproduction@gmail.com"
TWITTER_PASS = "Anton410101"


class InternetSpeedBot():
    def __init__(self):
        s = Service("/Users/antonyusupov/Desktop/Selenium/chromedriver")
        self.driver = webdriver.Chrome(service=s)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        start_button.click()
        time.sleep(45)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        return (float(self.down), float(self.up))

    def tweet(self, speed):
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR, '.css-1dbjc4n.r-2o02ov a')
        self.driver.execute_script("arguments[0].click();", sign_in_button)
        # sign_in_button.click()
        time.sleep(4)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_LOG)
        email.send_keys(Keys.ENTER)
        time.sleep(4)

        username = self.driver.find_element(By.CSS_SELECTOR, '.css-901oao.r-1awozwy.r-6koalj.r-37j5jr.r-1inkyih.r-16dba41.r-135wba7.r-bcqeeo.r-13qz1uu.r-qvutc0 input')
        username.send_keys(USERNAME)
        username.send_keys(Keys.ENTER)
        time.sleep(4)

        try:
            password = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASS)
            password.send_keys(Keys.ENTER)
            time.sleep(4)
        except:
            username = self.driver.find_element(By.CSS_SELECTOR,
                                                '.css-901oao.r-1awozwy.r-6koalj.r-37j5jr.r-1inkyih.r-16dba41.r-135wba7.r-bcqeeo.r-13qz1uu.r-qvutc0 input')
            username.send_keys(USERNAME)
            username.send_keys(Keys.ENTER)
            time.sleep(4)

            password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASS)
            password.send_keys(Keys.ENTER)
            time.sleep(4)


        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()
        time.sleep(4)

        message = self.driver.find_element(By.CSS_SELECTOR, '.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
        message.send_keys(f"Hey, why is my down speed is only {speed[0]} and my up speed is {speed[1]}")

        tweet = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet.click()


bot = InternetSpeedBot()
current_speed = bot.get_internet_speed()

if current_speed[0] < PROMISSED_DOWN or current_speed[1] < PROMISSED_UP:
    print("tweet")
    bot.tweet(current_speed)

