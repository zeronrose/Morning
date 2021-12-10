import requests,csv
from bs4 import  BeautifulSoup

def news():
	for hi in range(1,3):	
		url='https://news.ycombinator.com/news?p='+str(hi)
		Soup=BeautifulSoup(requests.get(url).text,'lxml')
		# House=Soup.find_all(class_='athing')
		smallbox=Soup.find('td',class_='subtext')		
		score=smallbox.find('span',class_='score').text
		age=smallbox.find('span',class_='age').text
		countcomments=(list(smallbox.find_all('a'))[3].text).replace(' ',' ')
		gtlnkkcoments=(list(smallbox.find_all('a'))[3])['href']
		comments='https://news.ycombinator.com/'+str(gtlnkkcoments)
		
news()
