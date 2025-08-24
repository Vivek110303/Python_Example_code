import csv

from web_3 import soup

data = [tag.text for tag in soup.find_all('h2')]
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for item in data:
        writer.writerow([item])
