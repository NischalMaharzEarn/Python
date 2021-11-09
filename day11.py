# Web scraping = extracting data from websites
import numpy
import requests
from bs4 import BeautifulSoup
r = requests.get('https://news.ycombinator.com/')

print(r.status_code) # requested code for retrieving file from the server
q = requests.get('https://news.ycombinator.com/')
#print(q.content)

# beauti bytes to html
soup = BeautifulSoup(r.content,'html.parser')
#print(soup.prettify())
#clearprint(soup.findAll('title'))
#('table',class_ = 'itemlist')) # prints class under table
print(soup.select('.itemlist')) # prints all class given itemlist
print(soup.selectone('.itemlist',prettify())) # prints all class given itemlist
newslist = soup.select('storylink')



for news in newslist:
    print(news.text)
    print(news.get('href'))

with open('jobs.txt','w') as f:
    for news in newslist:
        f.write(news.get('href') + '    ')
        f.write(news.text)
        f.write('/n','*'*20)