import requests
from bs4 import BeautifulSoup

from web_1 import response

soup = BeautifulSoup(response.content, 'lxml')
print(soup.prettify()[:500])  # Pretty print first 500 chars of HTML
