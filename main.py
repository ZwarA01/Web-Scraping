from bs4 import BeautifulSoup
import requests
import pandas
from scrapers.goodreadsScraper import goodreadsScraper
from scrapers.goodreadsSearch import goodreadsSearch
headers = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:138.0) Gecko/20100101 Firefox/138.0"
}

# url = "https://www.goodreads.com/shelf/show/goodreads-most-read-this-week"

# df = goodreadsScraper(url, headers)
# print(df)

print (goodreadsSearch(headers, 'diary of'))
