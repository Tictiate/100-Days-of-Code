import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome browser on
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(3)

lang_selector_button = driver.find_element(By.CSS_SELECTOR, ".langSelectButton")
lang_selector_button.click()

time.sleep(2)

button = driver.find_element(By.CSS_SELECTOR, "#bigCookie")

timeout = time.time() + 60*5 # 5 minutes from now
interval = time.time() + 60
x = 5

def click_button():
    five_seconds = time.time() + x
    while True:
        button.click()
        if time.time() > five_seconds:
            break

def check_upgrade():
    unlocked = driver.find_elements(By.CSS_SELECTOR, ".enabled")
    div =  unlocked[-1]
    div.click()

while True:
    click_button()
    check_upgrade()
    if time.time() > timeout:
        break
    if time.time() > interval:
        interval = time.time() + 60
        x += 5

cookies = driver.find_element(By.CSS_SELECTOR, "#cookiesPerSecond").text
ls = cookies.split()
cookies_per_second = ls[-1]
print(cookies_per_second)


driver.quit()