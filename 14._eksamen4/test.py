import requests
from bs4 import BeautifulSoup

URL = "google"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
print(soup)