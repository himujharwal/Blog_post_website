import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.status_code)
print(response.json())


payload = {'userId':11, 'id':101, 'title':'well here i go', 'body': 'there you go here we go'}
response = requests.post('https://jsonplaceholder.typicode.com/posts/1', json=payload)

print(response.status_code)
print(response.json())