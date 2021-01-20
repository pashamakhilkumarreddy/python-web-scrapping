import logging, sys, requests, time
from bs4 import BeautifulSoup
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

URL: str = 'https://www.whitehouse.gov/about-the-white-house/presidents/'

def print_presidents(url):
  html_text = requests.get(url)
  soup = BeautifulSoup(html_text.content, 'lxml')
  # print(soup.prettify())
  presidents = []
  elements = soup.find_all('div' , class_ = 'grid-item__container')
  for element in elements:
    name = element.find('h3' , class_ = 'grid-item__title').text.strip()
    term = element.find('span', 'acctext--con').text.strip()
    presidents.append(f'{name} | {term}')

  max_length = max(list(map(lambda x: len(x), presidents)))
  for (index, president) in enumerate(presidents):
    print('-' * max_length)
    print(f'| {index + 1}. {president} |')
    print('-' * max_length)

if __name__ == '__main__':
  # Set the format for logging info
  logging.basicConfig(level = logging.INFO, format='%(asctime)s - %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')
  path = sys.argv[1] if len(sys.argv) > 1 else '.'
  event_handler = LoggingEventHandler()
  observer = Observer()
  observer.schedule(event_handler, path, recursive = True)
  observer.start()
  try:
    logging.info('Getting all US Presidents information')
    print_presidents(URL)
    logging.info('Waiting')
    time.sleep(300)
  except KeyboardInterrupt:
      observer.stop()
  observer.join()
