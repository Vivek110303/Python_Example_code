from web_3 import soup

data = {}
for idx, p in enumerate(soup.find_all('p')[:5]):
    data[f'paragraph_{idx+1}'] = p.text
print(data)
