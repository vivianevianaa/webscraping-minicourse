import requests
from bs4 import BeautifulSoup
#from colorama import Fore, Style, Back


URL = "https://www.google.com.br/"
my_page = requests.get(URL)

soup = BeautifulSoup(my_page.content, "html.parser")

#print(Fore.RED + "Title" + Style.RESETALL)
print(soup.title)

#print(Fore.BLUE + "Body" + Style.RESETALL)
print(soup.body)