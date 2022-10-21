import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# Sets up the webdriver which is in a local path
driver = webdriver.Chrome("C:/Users/ekant/Desktop/Python Practise/chromedriver.exe")
driver.get("https://www.speedtest.net/")

# Opens internet speed meter webpage and clicks the "GO" button
speed = driver.find_element('xpath', '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]')
speed.click()

# Waits for 50seconds for page the get internet speed rates and assign rates to variables
sleep(50)
up = driver.find_element('xpath', '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                  '3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
up_text = up.text
down = driver. find_element('xpath', '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                     '3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
down_text = down.text

# Turns off the browser
driver.close()

# Opens a new browser tab and goes to twitter login page
driver2 = webdriver.Chrome("C:/Users/ekant/Desktop/Python Practise/chromedriver.exe")
driver2.get("https://twitter.com/i/flow/login")

# Waits 5 seconds, places username and presses "ENTER" key
sleep(5)
email = driver2.find_element(By.TAG_NAME, 'input')
email.send_keys(os.environ['USER_NAME'], Keys.ENTER)

# Waits 5 seconds, places password and presses "ENTER" key
sleep(5)
password = driver2.find_element(By.NAME, 'password')
password.send_keys(os.environ['PASSWORD'], Keys.ENTER)

# Waits 5 seconds, places entry and posts it.
sleep(5)
entry = driver2.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
entry.send_keys(f'Hey AGL, why is my internet speed {down_text}Down and {up_text}Up when I pay for 25Down and 5Up '
                f'@AGLAustralia', Keys.CONTROL+Keys.ENTER)