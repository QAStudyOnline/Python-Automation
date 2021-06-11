import time

from selenium import webdriver

PATH_TO_CHROMEDRIVER = "004_lesson/resources/chromedriver.exe"

driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER)
driver.get("https://auto.ria.com/uk/")
