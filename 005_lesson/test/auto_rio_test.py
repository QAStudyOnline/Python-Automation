from page.auto_rio_page import AutoRioMainPage

def test_can_autorio_serach_audi_a6():
    page = AutoRioMainPage()
    page.select_car_type("Мото")
    page.start_search()
    assert page.get_amount_of_found_cars > 0
