import os

from django.contrib.sites import requests

from web_3 import soup

image_tags = soup.find_all('img')
image_urls = [img['src'] for img in image_tags if 'src' in img.attrs]

folder = 'downloaded_images'
os.makedirs(folder, exist_ok=True)

for i, url in enumerate(image_urls[:5]):
    try:
        img_data = requests.get(url).content
        filename = os.path.join(folder, f'image_{i+1}.jpg')
        with open(filename, 'wb') as file:
            file.write(img_data)
        print(f'Downloaded {filename}')
    except Exception as e:
        print(f"Could not download {url}: {e}")
