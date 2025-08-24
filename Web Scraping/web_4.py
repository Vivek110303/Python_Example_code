import requests
from bs4 import BeautifulSoup

from web_1 import response
from web_3 import soup

# Example: extract all paragraph texts
paragraphs = [p.text for p in soup.find_all('p')]
print(paragraphs)
