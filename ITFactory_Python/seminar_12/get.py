import requests
from pprint import pprint

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)
pprint(response.__dict__)
if response.status_code == 200:
	data = response.json()
	print(data)
else:
	print('Request failed with status code:',response.status_code)