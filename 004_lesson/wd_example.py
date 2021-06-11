import time

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

PATH_TO_CHROMEDRIVER = "004_lesson/resources/chromedriver.exe"
PATH_TO_FIREFOX = "004_lesson/resources/geckodriver.exe"
GOOGLE_URL = "http://www.google.com/"

profile = webdriver.FirefoxProfile()
binary = FirefoxBinary(PATH_TO_FIREFOX)
driver = webdriver.Firefox(firefox_profile=profile, executable_path=PATH_TO_FIREFOX)
driver.get(GOOGLE_URL)
time.sleep(2)
title = driver.title
assert title == 'Google'
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(2)
driver.quit()
