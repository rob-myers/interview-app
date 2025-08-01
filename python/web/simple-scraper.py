import requests

search_term='foo'

res = requests.get(f'https://www.google.com/search?q={search_term}')

print(res.text)