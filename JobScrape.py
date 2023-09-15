from bs4 import BeautifulSoup
import lxml
import requests
import time

print("Type in skills you are unfamiliar with")
unfamiliar_skill = input(">")
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():
  html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
  soup = BeautifulSoup(html_text, 'lxml')
  jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
  for job in jobs:
    date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in date:
      company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
      skill_req = job.find('span', class_ = 'srp-skills').text.replace(' ','')
      more_info = job.header.h2.a['href']
      if unfamiliar_skill not in skill_req:
        print(f"Company Name: {company_name}".strip())
        print(f"Required Skills: {skill_req}".strip())
        print(f"More Info: {more_info}")

        print(' ')

#if __name__ == '__main__:
#  'while True:
find_jobs()
time_wait = 10
print(f"Waiting {time_wait} minutes...")
time.sleep(time_wait * 60)
