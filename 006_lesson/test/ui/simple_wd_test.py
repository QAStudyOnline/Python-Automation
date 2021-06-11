import allure
import time

from selenium import webdriver

PATH_TO_CHROMEDRIVER = "004_lesson/resources/chromedriver.exe"
GOOGLE_URL = "http://www.google.com/"

@allure.feature("Open google")
@allure.story("Able to open the ggole from python and selenium")
@allure.description("In thin test I have to verify that I can open the google")
@allure.step("Test can open the google")
def test_can_open_google():
    driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER)
    driver.get(GOOGLE_URL)
    time.sleep(5)
    title = driver.title
    assert title == 'Google'
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)
    driver.title
    driver.quit()
