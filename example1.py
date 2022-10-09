import requests

URL = "https://www.google.com.br/"

my_page = requests.get(URL)

print(my_page.headers)
print("\n")
print(my_page.content)
print("\n")
print(my_page.text)