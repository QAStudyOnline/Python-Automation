from selenium import webdriver
from selenium.webdriver.support.select import Select


class AutoRioMainPage():

    def __init__(self):
        self.driver = webdriver.Chrome("005_lesson/resources/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://auto.ria.com/uk/")

    def select_car_type(self, car_type):
        car_type_select = Select(self.driver.find_element_by_id("categories"))
        car_type_select.select_by_index(2)

        # car_type = self.driver.find_element_by_id("categories")
        # car_type.click()
        # car_type_select = Select(self.driver.find_element_by_id("categories"))
        # car_type_select.select_by_visible_text(car_type)

        # car_type_select = Select(self.driver.find_element_by_id("categories"))
        # if car_type == "Мото":
        #     car_type_select.select_by_value(str(2))

    def start_search(self):
        self.driver.find_element_by_css_selector(".button").click()

    def get_amount_of_found_cars(self):
        return len(self.driver.find_elements_by_css_selector(".content-bar"))
