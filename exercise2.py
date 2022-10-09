from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

URL = "https://eventos.unichristus.edu.br/"

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
  site = soup.find("div", {"class": "eventos"})

  events = site.find_all(["h4", {"class": "timeline-item-title"}])

  events_title = []
  for event in events:
    title = event.find("span", {"class": "truncate"})
    events_title.append(title.text)
  for e in events_title:
    print(e)

    
