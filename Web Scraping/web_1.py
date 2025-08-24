import requests

url = "https://example.com"
response = requests.get(url)
print(response.status_code)  # Should be 200 if successful
print(response.text[:500])   # Print first 500 characters of page
