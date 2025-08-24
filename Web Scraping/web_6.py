
from web_3 import soup

items = [item.text for item in soup.select('div.classname')]
print(items)
