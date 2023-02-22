import requests


url = "https://jsonplaceholder.typicode.com/posts"

payload = {
	"userId": 10,
	"title": "postare frumoasa",
	"body": "cea mai frumoasa postare"
}

response = requests.post(url, json=payload)
if response.status_code == 201: # 201 = created
	data = response.json()
	print(data)
else:
	print('Request failed with status code:',response.status_code)
