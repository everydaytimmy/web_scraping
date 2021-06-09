import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/House_of_Romanov"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

links = soup.find_all('a', href='/wiki/Wikipedia:Citation_needed')

def get_citation(links):
  counter = 0
  for a_tag in links:
    counter += 1
    print(a_tag.parent.parent.parent.get_text())
  print(f"There are {counter} citations needed on this page")
    

get_citation(links)