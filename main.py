from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time

ACC_EMAIL = "xxx"
ACC_PASS = "xxx"

HEADERS = {'User Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
            "Accept-Language": "en-US,en;q=0.9"}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3559393578&f_E=2&geoId=90010472&keywords=python%20developers&location=San%20Diego%20Metropolitan%20Area&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# click sign in button
time.sleep(5)
sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

# enter logins
time.sleep(5)
user_login = driver.find_element(By.ID, "username")
user_login.send_keys(ACC_EMAIL)
user_pass = driver.find_element(By.ID, "password")
user_pass.send_keys(ACC_PASS)
user_pass.send_keys(Keys.ENTER)

time.sleep(5)
save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
save_button.click()

# a class nav__button-secondary

