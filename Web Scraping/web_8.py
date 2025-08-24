from django.contrib.sites import requests
import requests
from bs4 import BeautifulSoup

from web_1 import response
from web_3 import soup

post_url = "https://example.com/form"
data = {'key1': 'value1', 'key2': 'value2'}
response_post = requests.post(post_url, data=data)
print(response_post.status_code)
print(response_post.text[:300])
