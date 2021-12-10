import requests,csv
from bs4 import  BeautifulSoup


# url='https://news.ycombinator.com/news?p=1'
# Soup=BeautifulSoup(requests.get(url).text,'lxml')

# texts=Soup.find_all('td',class_ ='subtext')
# for hi in texts:
# 	score=hi.find('span',class_='score')
# 	if score:
# 		print(score.text)
# 	elif score==None:
# 		print('hi')
def news():
	for hi in range(1,3):	
		url='https://news.ycombinator.com/news?p='+str(hi)
		Soup=BeautifulSoup(requests.get(url).text,'lxml')
		hi=Soup.find_all(class_='athing')
		for Box in hi:
			Points=[]
			Title=Box.find('a',class_='titlelink').text
			link=Box.find('a',class_='titlelink')['href']
			Footer=Soup.find_all('td',class_='subtext')
			for smallbox in Footer: 
				scores=smallbox.find('span',class_='score')
				Number=scores.text if score else "No data Found"
				print(Number)


				
			age=smallbox.find('span',class_='age').text
			countcomments=(list(smallbox.find_all('a'))[3].text).replace(' ',' ')
			gtlnkkcoments=(list(smallbox.find_all('a'))[3])['href']
			comments='https://news.ycombinator.com/'+str(gtlnkkcoments)
			# with open('Yhacker.csv',newline='',mode='a+') as fire:
			# 	spam=csv.writer(fire,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			# 	spam.writerow([Title,link,Points,age,countcomments,comments])

news()