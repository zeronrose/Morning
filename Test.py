import requests,csv
from bs4 import  BeautifulSoup


url='https://news.ycombinator.com/news?p=1'
Soup=BeautifulSoup(requests.get(url).text,'lxml')

hi=Soup.find_all('td',class_='subtext')
for smallbox in hi:
	score= (smallbox.find('span',class_='score')).text.replace(' points','')
	print(score)

	# try:
	# 	po=score if len(score)>1 else "SOrry"
	# 	print(po)
	# except AttributeError as hi:
	# 	print("NONO",hi)

	# a=(smallbox.find('span',class_='score'))
	# print(a)

	# print(score.text.replace(' points',''))
	# age=smallbox.find('span',class_='age').text
	# countcomments=(list(smallbox.find_all('a'))[3].text).replace(' ',' ')
	# gtlnkkcoments=(list(smallbox.find_all('a'))[3])['href']
	# comments='https://news.ycombinator.com/'+str(gtlnkkcoments)
	# print(score)	
	# print(countcomments)