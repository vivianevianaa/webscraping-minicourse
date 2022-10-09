import os
import csv
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

URL = "https://www.ofertaesperta.com/"

my_page = requests.get(URL)
html = my_page.content.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

offer_previous = soup.find_all("div", {"class": "offer-previous-price"})
offer_discount = soup.find_all("div", {"class": "offer-card-price"})

print("Price Previous")
previous_price = []
for previous in offer_previous:
  previous_price.append(previous.text)
print(previous_price)

print("Prices with Discounts")
discount_price = []
for discount in offer_discount:
  integer = discount.find("span", {"class": "offer-card-price-integer"}).get_text()
  decimal = discount.find("span", {"class": "offer-card-price-decimal"})
  if (decimal == None):
    decimal = ",00"
    price = integer + decimal
  else:
    price = integer + decimal.get_text()
  discount_price.append(price)
print(discount_price)

# try:
#   my_page = urlopen(URL)
# except HTTPError as e:
#   print('HTTP ERROR')
#   print(e.code)
# except URLError as e:
#   print('URL ERROR')
#   print(e.reason)
# else:
#   soup = BeautifulSoup(my_page.read(), "html.parser")
#   offer_previous = soup.find_all("div", {"class": "offer-previous-price"})
#   offer_descount = soup.find_all("div", {"class": "offer-card-price"})

#   previous_price = []
#   for previous in offer_previous:
#     previous_price.append(previous.text)
#   print(previous_price)