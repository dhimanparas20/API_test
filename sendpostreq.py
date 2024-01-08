# Code to understand how to send post req in python
import requests

url = 'http://127.0.0.1:5000/changepass'
payload = {
    'email': 'gokew42094@tanlanav.com',
    'currentpassword': '12345678',
    'newpassword':"1234567890"

}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print('Request successful!')
    print('Response:', response.text)
else:
    print('Request failed with status code:', response.status_code)
