from pprint import pprint

import requests


url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {
	"userId": 10
}
# PATCH - face update doar la partea din resursa specificata in payload
response = requests.patch(url, json=payload)
if response.status_code == 200:
	data = response.json()
	pprint(data)
else:
	print('Request failed with status code:', response.status_code)
