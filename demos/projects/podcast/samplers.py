import requests

result = requests.get("https://www.oreilly.com/free/")

print(result.status_code)
print(result.headers)

c = result.content
from bs4 import BeautifulSoup

soup = BeautifulSoup(c, 'lxml')
samples = soup.find_all("a", "item-title")
print('xyz')
print(samples[:5])
print('abc')
data = {}
for a in samples:
    print('a', a)
    title = a.string.strip()
    print('title', title)
    print("string", a.string)
    data[title] = a.attrs['href']
    print("attrs", a.attrs['href'])
    print("attrs2", a.attrs)
    del a.attrs['class']
    print("attrs2", a.attrs)

print(data)
print(list(data)[:5])
#

