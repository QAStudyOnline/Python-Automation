import pytest
import requests
import json
import request_example as re


class TestAPI:
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

    def test_can_get_user_by_name(self):
        username = 'TestPython'
        # Pre-Condition
        re.send_post_request(username)

        # Test Step
        resp = requests.get(f"https://petstore.swagger.io/v2/user/{username}",
                            headers={"accept": "application/json", "Content-Type": "application/json"})
        # Post-Condition cleanup environment
        # delete_user_by_user_name(username)

        # Verification
        assert resp.status_code == 200
        assert resp.json()['username'] == 'TestPython'

