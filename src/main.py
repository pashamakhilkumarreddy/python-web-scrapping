import requests
from bs4 import BeautifulSoup

URL: str = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'

page: str = requests.get(URL)

soup = BeautifulSoup(page.text, 'lxml')

print(f'HTML content {soup.prettify()}')

H1 = {soup.find('h1')}

print(f'H1 {H1}')
p_tags = soup.find_all('p')
print(f'P tags {p_tags}')

for tag in p_tags:
  print(tag.text)

chorus = soup.find_all('p', class_='chorus')
print(f'Chorus {chorus}')

for c in chorus:
  print(c.text)
