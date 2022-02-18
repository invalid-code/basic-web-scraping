from bs4 import BeautifulSoup 
import requests as rq 
url = "https://kumascans.com/"
requesting_url = rq.get(url)
html_doc_soup = BeautifulSoup(requesting_url.text, "html.parser")
print(html_doc_soup.prettify())