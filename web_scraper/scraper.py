import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/House_of_Romanov"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

links = soup.find_all('a', href='/wiki/Wikipedia:Citation_needed')

def citation_report(links):
  for a_tag in links:
    print(a_tag.parent.parent.parent.get_text())
  

def citations_count(links):
  counter = 0
  for i in links:
    counter += 1
  print(f"There are {counter} citations needed on this page")
    

citations_count(links)

citation_report(links)