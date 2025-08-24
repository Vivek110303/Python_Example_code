# 1. Filter by tag and attribute
filtered = soup.find_all('a', href=True)
# 2. Filter by text containing a word
filtered = soup.find_all(string=lambda text: 'Python' in text)
# 3. Filter with CSS selectors
filtered = soup.select('div#main-content p.highlight')
# 4. Combined filter example
filtered = [tag for tag in soup.find_all('li') if 'data' in tag.text.lower()]
print(filtered)
