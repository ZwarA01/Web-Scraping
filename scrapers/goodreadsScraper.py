from bs4 import BeautifulSoup
import requests
import pandas
import re

def goodreadsScraper(url, headers):
  get = requests.get(url, headers = headers) # get request to goodreads; headers needed to trick website into thinking a bot isn't scraping
  soup = BeautifulSoup(get.text, "lxml") # the whole page in html

  title = soup.find_all("a", class_ = 'bookTitle') # find all 'a' tags with class 'bookTitle"
  titles = [item.text.strip() for item in title] # create list of all book titles without extra html

  author = soup.find_all("a", class_ = 'authorName') # find all 'a' tags with class "authorName"
  authors = [item.text.strip() for item in author] # create list of all authors without extra html

  rating = soup.find_all(class_ = 'greyText smallText') # find all tags with class name "minirating"
  ratings = [item.text.strip() for item in rating] # create list of all ratings
  
  cleanRatings = [] # list of ratings without words
  for r in ratings:
      match = re.search(r'\d+\.\d+', r)  # Finds first float with regex 
      if match:
          cleanRatings.append(match.group() + '/5.00') # returns float group 
      else:
          cleanRatings.append(None)  # or handle missing/invalid case
          
  df = pandas.DataFrame({ # create table, header:info
        'Title': titles,
        'Author': authors,
        'Rating': cleanRatings
    })
  return df

  
