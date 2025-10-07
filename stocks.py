from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def scrape(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html,"html.parser")

    souplist_raw = soup.get_text().split("\n")
    print(souplist_raw)

scrape("https://finance.yahoo.com/quote/CSCO/")