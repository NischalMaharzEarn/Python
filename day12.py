import requests
from bs4 import BeautifulSoup
r = requests.get('https://broadwayinfosys.com/career')

print(r.status_code) 



title = BeautifulSoup(r.content,'html.parser')

jobs = (title.select('.block-card'))


with open('jobs.txt','w') as j:
    for job in jobs:
        j.write(job.select_one('.content-title').text + '    ')
        j.write(job.find('a').get('href') + '\n' + '*'*5)

