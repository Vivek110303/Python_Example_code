from django.contrib.sites import requests
import requests
from bs4 import BeautifulSoup

from web_ import response
from web_3 import soup
params = {'search': 'python', 'page': 2}
response = requests.get(url, params=params)
print(response.url)  # Shows full URL with parameters
