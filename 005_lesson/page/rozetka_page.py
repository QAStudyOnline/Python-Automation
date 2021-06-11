from selenium import webdriver


class RozetkaMainPage():

    def __init__(self):
        self.driver = webdriver.Chrome("005_lesson/resources/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://rozetka.com.ua/")

    def search_item(self, item_name):
        search_field = self.driver.find_element_by_name("search")
        search_field.clear
        search_field.send_keys(item_name)

    def start_search(self):
        search_btn = self.driver.find_element_by_css_selector(".button.button_color_green")
        search_btn.click()

    def get_amount_of_found_goods(self):
        return len(self.driver.find_elements_by_css_selector(".goods-tile__picture"))