import os
import csv
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

path = os.path.join("logs")
if not os.path.exists(path):
  os.mkdir(path)
csv_file = open(path+"/events.csv", "w")
try:
  writer = csv.writer(csv_file, delimiter=",")
  writer.writerow(['events'])
  for event in events_title:
    writer.writerow([event])
except FileNotFoundError as e:
  print(e)
csv_file.close()
