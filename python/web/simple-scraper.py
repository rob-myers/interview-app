# pip3 install requests
import requests
# from xml.dom import minidom
# pip3 install beautifulsoup4
from bs4 import BeautifulSoup

search_term='foo'

res = requests.get(f'https://www.google.com/search?q={search_term}')

# print(res.text)
# parsed = minidom.parseString('<foo></foo>')
# parsed = minidom.parseString(res.text) # ❌

parsed = BeautifulSoup(res.text, 'html.parser')
print(parsed.prettify())