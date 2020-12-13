import requests
import time
import sys
import logging
import os
from bs4 import BeautifulSoup
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

URL: str = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=golang&txtLocation='

def find_jobs(): 
  html_text = requests.get(URL)

  soup = BeautifulSoup(html_text.text, 'lxml')

  # print(soup)

  print('Enter any skill that you are not familiar with')

  unfamiliar_skill = input('>')

  jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')

  for index, job in enumerate(jobs): 
    published_date = job.find('span', class_ = 'sim-posted').span.text.strip()
    if 'few' in published_date:
      company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip().replace(' ', '')
      skills = job.find('span', class_ = 'srp-skills').text.strip().replace(' ', '')
      more_info = job.header.h2.a['href']
      if unfamiliar_skill not in skills:
        file_name = f'{index}.txt'
        with open(f'jobs/{file_name}', 'w') as file:
          file.write(f'Company Name: {company_name} \n')
          file.write(f'Skills: {skills} \n')
          file.write(f'Published Date: {published_date} \n')
          file.write(f'More Info: {more_info} \n')
          # print(f'''
          #   Job {job}
          #   Company Name {company_name}
          #   Skills {skills}
          #   Published Date {published_date}
          #   More Info {more_info}
          # ''')  
          print(f'File saved {file_name}')

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
  path = sys.argv[1] if len(sys.argv) > 1 else '.'
  event_handler = LoggingEventHandler()
  observer = Observer()
  observer.schedule(event_handler, path, recursive = True)
  observer.start()
  try:
    while True:
      dirs = os.listdir('.')
      if not 'jobs' in dirs:
        os.mkdir('jobs')
      find_jobs()
      print(f'Waiting')
      time.sleep(300)
  finally:
    observer.stop()
    observer.join()
