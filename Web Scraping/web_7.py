from web_3 import soup

clean_text = [tag.get_text(strip=True) for tag in soup.find_all('h2')]
print(clean_text)
