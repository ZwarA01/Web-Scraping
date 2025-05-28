from bs4 import BeautifulSoup
import requests
import pandas
import re
from dotenv import load_dotenv
import os
from goodreadsSearch import goodreadsSearch

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:138.0) Gecko/20100101 Firefox/138.0"
    }

load_dotenv()  # Loads values from .env into environment
api_key = os.getenv("NYT_BOOKS_API_KEY")
url = f"https://api.nytimes.com/svc/books/v3/lists/overview.json?api-key={api_key}"
response = requests.get(url)

data = response.json()

for bestseller_list in data['results']['lists']:
    print(f"\n📚 {bestseller_list['list_name']}")
    
    for book in bestseller_list['books']:
        title = book['title']
        author = book['author']
        rank = book['rank']

        try:
            rating = goodreadsSearch(headers, title)
        except Exception as e:
            rating = f"Error: {e}"

        print(f"  {rank}: {title} by {author} — Goodreads Rating: {rating}")

def weeklyBestSellers():
  print('s')