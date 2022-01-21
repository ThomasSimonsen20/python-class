import requests
from bs4 import BeautifulSoup

URL = "https://webscraper.io/test-sites/e-commerce/allinone"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
print(page.content)