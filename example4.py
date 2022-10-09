import requests
from bs4 import BeautifulSoup
#from colorama import Fore, Style
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

URL = "https://unichristus.edu.br"
# my_page = requests.get(URL)

try:
  my_page = urlopen(URL)
except HTTPError as e:
  print("HTTP ERROR")
  print(e.code)  
except URLError as e:
  print("URL ERROR")
  print(e.reason)
else:
  soup = BeautifulSoup(my_page.read(), "html.parser")
  uni_news = soup.find("div", {"class": "wgt-outras-noticias"})
  #print(uni_news.prettify())
  
  events = uni_news.find_all(["a"])
  #print(events)

  for event in events:
    print(event.get_text())
