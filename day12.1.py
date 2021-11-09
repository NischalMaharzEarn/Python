import requests # Code to get required jobs directly from merojob.
from bs4 import BeautifulSoup
a = input('Which job are you searching for ?')
link = requests.get(f'https://merojob.com/search/?q={a}')
title = BeautifulSoup(link.content,'html.parser')
jobs = title.select('.media-heading')

with open('merojobs.txt','w') as m:
    for job in jobs:
        m.write(job.text + '    ')
        m.write(job.find('a').get('href') + '\n' + '*'*5)
    m.close()
