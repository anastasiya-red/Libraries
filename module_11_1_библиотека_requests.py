from requests import get

r = get('https://grasser.ru/vykrojki/')
print(r.headers)
print(r.text)
