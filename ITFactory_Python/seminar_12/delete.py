import requests


url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

if response.status_code == 200:
	data = response.json()
	print(data)
else:
	print('Request failed with status code:', response.status_code)
