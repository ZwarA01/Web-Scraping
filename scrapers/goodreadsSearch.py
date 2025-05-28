import time
from bs4 import BeautifulSoup
import requests
import pandas
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:138.0) Gecko/20100101 Firefox/138.0"
    }
    
def goodreadsSearch(headers, title, author=''):

    query = f"{title} {author}"
    query = query.replace(" ", "+")  # spaces turn into + for search ability
    url = f"https://www.goodreads.com/search?q={query}"
    time.sleep(.001)
    get = requests.get(url, headers=headers)  # get request to goodreads; headers needed to trick website into thinking a bot isn't scraping
    soup = BeautifulSoup(get.text, "lxml")  # the whole page in html

    titleContainer = soup.find("span", attrs={"itemprop": "name", "aria-level": "4"})  # find 'span' tags with class 'name' and aria-level 4 for book title
    if titleContainer:
        titleName = titleContainer.text.strip()
    else:
        return 'Book does not exist'

    authorContainer = soup.find("div", class_="authorName__container")
    if authorContainer:
        authorHtml = authorContainer.find("span", itemprop="name")  # type: ignore
        if authorHtml:
            authorName = authorHtml.text.strip()
        else:
            return 'Book does not exist'
    else:
        return 'Book does not exist'
    
    ratingContainer = soup.find("span", class_="minirating")
    if ratingContainer:
        ratingText = ratingContainer.text.strip()
        match = re.search(r'\d+\.\d+', ratingText)
        if match:
            cleanRating = match.group() + '/5.00'
        else:
            cleanRating = None
    else:
        cleanRating = None
        
    return cleanRating # just need rating for now
