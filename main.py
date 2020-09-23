import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from time import sleep
from random import randint

headers = {"Accept-Language": "en-US, en;q=0.5"}

# main url for programming jobs 
url = "https://weworkremotely.com/categories/remote-programming-jobs#job-listings"

results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, "html.parser")

# select section where jobs exist
job_section = soup.find('section', class_='jobs')
jobs = job_section.find_all('li')


#create empty lists to store data
companies = []
titles = []
types = []
locations = []
links = []
logos = []
overviews = []

# initiate for loop
for item in jobs:
  #extract company name
  company = item.find_all('span', class_='company')
  name = company[0].text if len(company) > 0 else '-'
  companies.append(name)

  type = company[1].text if len(company) > 1 else '-'
  types.append(type)

  location = item.find('span', class_='region company').text if item.find('span', class_='region company') else '-'
  locations.append(location)

  title = item.find('span', class_='title').text if item.find('span', class_='title') else '-'
  titles.append(title)

 # extract only the link that takes the user to the job detail page
  link = '-'
  for a in item.find_all('a', href=True):
    if (a['href']).startswith('/remote-jobs'):
      link = (a['href']) 
  links.append(link)

# extract only the link that takes user to the company overview page
  overview = '-'
  for a in item.find_all('a', href=True):
    if (a['href']).startswith('/company'):
      overview = (a['href']) 
  overviews.append(overview)

  img = '-'
  if item.find('div', class_='flag-logo'):
    img = item.find('div', class_='flag-logo')['style']
    img = img[21:-1] 
  else: 
    '-'
  logos.append(img)

jobs = pd.DataFrame({
  'company': companies,
  'type': types,
  'location': locations,
  'title': titles,
  'link': links,
  'logo': logos,
  'company_overview': overviews
})

print(jobs)
jobs.to_csv('jobs.csv')



