import requests
import json

url = "https://petstore.swagger.io/v2/user"

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


def send_post_request(name_of_test_user):
    user_name = f"{name_of_test_user}"
    request_body = json.dumps({
        "id": 123455555555,
        "username": f"{user_name}",
        "firstName": "Test1",
        "lastName": "Test1",
        "email": "Test1@Test1.com",
        "password": "Test1",
        "phone": "+380659998877",
        "userStatus": 0
    })
    return requests.post(url, headers=headers, data=request_body)


def send_get_request(name_of_user):
    return requests.get(url + f"/{name_of_user}", headers=headers)


# Send POST request and print results
print("""
Send POST request and print results
""")
response_post = send_post_request("Python_TestUser_1")

print(response_post.json())
print(response_post.json()['code'])
print(response_post.json()['type'] == 'unknown')
print(response_post.status_code == 200)

# Send GET request ad print results
print("""
Send GET request ad print results
""")
response_get = send_get_request("Python_TestUser_1")
print(response_get.json()['username'])
print(response_get.json()['username'] == "Python_TestUser_1")
