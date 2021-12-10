import requests,csv
from bs4 import  BeautifulSoup


url='https://news.ycombinator.com/news?p=1'
Soup=BeautifulSoup(requests.get(url).text,'lxml')

texts=Soup.find_all('td',class_ ='subtext')
for hi in texts:
	score=hi.find('span',class_='score')
	if score:
		print(score.text)
	elif score==None:
		print('hi')
