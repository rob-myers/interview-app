# pyright: reportUnknownMemberType=false
# pyright: reportUnknownArgumentType=false
# pyright: reportAttributeAccessIssue=false

# pip3 install requests
import requests
# from xml.dom import minidom
# pip3 install beautifulsoup4
from bs4 import BeautifulSoup

search_term='bar+baz'

# res = requests.get(f'https://www.google.com/search?q={search_term}')
res = requests.get(f'http://localhost:3000/blog/about')

# print(res.text)
# parsed = minidom.parseString('<foo></foo>')
# parsed = minidom.parseString(res.text) # ❌

parsed = BeautifulSoup(res.text, 'html.parser')
# print(parsed.prettify())


anchors = parsed.find_all('a')

for anchor in anchors:
  print(anchor.get('href'))