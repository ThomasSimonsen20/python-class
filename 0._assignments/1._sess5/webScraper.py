import requests
#from bs4 import BeautifulSoup
from markdownify import markdownify

URL = "https://clbokea.github.io/exam/assignment_2.html"
page = requests.get(URL)

markdown = markdownify(page, heading_style="ATX")

print(markdown)

#soup = BeautifulSoup(page.content, "html.parser")
#results = soup.find(id="job-ad-summary")