from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

URL = "https://maumneto.github.io/mauriciomoreira/"

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
  site = soup.find("div", {"class": "resume-content"})
  
  headers = site.find_all(["h4", "h5"])

  for disc in headers:
    print(disc.text)
