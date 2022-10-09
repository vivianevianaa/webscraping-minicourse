import re

with open("logs/text.txt", "r") as my_file:
  text = my_file.read()
  my_first_regex = re.findall("et", text)
  #print(text)
  print(len(my_first_regex))