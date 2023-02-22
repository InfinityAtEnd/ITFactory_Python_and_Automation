from pprint import pprint

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {
	"userId": 10,
	"comment": "actualiza cu PUT method",
	"title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
	"body": "quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
# PUT - va incerca sa acctualizeze intreaga resurse(sterge campurile nespecificate in payload)
response = requests.put(url, json=payload)
if response.status_code == 200:
	data = response.json()
	pprint(data)
else:
	print('Request failed with status code:', response.status_code)
