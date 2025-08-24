import requests
from web_1 import response
response.encoding = 'utf-8'
content = response.text
print(content[:200])
