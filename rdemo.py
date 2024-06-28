import requests

r = requests.get('https://www.instagram.com/23rdlegend/')

r.text

with open('comic.png', 'wb') as f:
    f.write(r.content)

print(r.headers)

payload = {'page': 2, 'count': 25}

k = requests.get('https://httpbin.org/get', params=payload)

print(k.url)

load = {'username': 'ssekwe', 'password': 'testing'}

j = requests.post('https://httpbin.org/post', data=load)

j_dict = j.json()

print(j_dict)

q = requests.get('https://httpbin.org/basic-auth/ssekwe/testing', auth=('ssekwe', 'testing'))

print(q.text)


