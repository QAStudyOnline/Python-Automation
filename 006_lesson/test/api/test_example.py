import allure
import requests
import json

@allure.feature("API Tests")
@allure.story("Verify that I able to create user via the API calls")
class TestAPI:
    @allure.step("Create User vea the POST request")
    def test_can_create_user(self):
        user = json.dumps({
            "id": 12231221213,
            "username": "TestPython",
            "firstName": "TestPython",
            "lastName": "TestPython",
            "email": "TestPython@gmail.com",
            "password": "TestPython",
            "phone": "+380975568795",
            "userStatus": 0
        })
        resp = requests.post("https://petstore.swagger.io/v2/user/",
                             headers={"accept": "application/json", "Content-Type": "application/json"}, data=user)
        assert resp.status_code == 200
        assert resp.json()['code'] == 200

    @allure.step("Read user info via GET request")
    def test_can_get_user_by_name(self):
        username = 'TestPython'

        # Test Step
        resp = requests.get(f"https://petstore.swagger.io/v2/user/{username}",
                            headers={"accept": "application/json", "Content-Type": "application/json"})
        # Post-Condition cleanup environment
        # delete_user_by_user_name(username)

        # Verification
        assert resp.status_code == 200
        assert resp.json()['username'] == 'TestPython'

