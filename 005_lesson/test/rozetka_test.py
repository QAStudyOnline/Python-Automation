from page.rzetka import RozetkaMainPage


def test_can_rozetka_found_iphone():
    page = RozetkaMainPage()
    page.search_item("iphone 12 pro max 512")
    page.click()
    assert page.get_amount_of_found_goods() > 0
