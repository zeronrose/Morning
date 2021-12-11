import requests,csv
from bs4 import  BeautifulSoup


# url='https://news.ycombinator.com/news?p=1'
# Soup=BeautifulSoup(requests.get(url).text,'lxml')


# for hi in range(1,3):	
# 		url='https://news.ycombinator.com/news?p='+str(hi)
# 		Soup=BeautifulSoup(requests.get(url).text,'lxml')
# 		# hi=Soup.find_all(class_='athing')
# 		texts=Soup.find_all('td',class_ ='subtext')
# 		for smallbox in texts:
# 			try:
# 				countcomments=(list(smallbox.find_all('a'))[3])
# 				haha=countcomments.text.replace(' ',' ') if countcomments else "No data Found"
# 				gtlnkkcoments=(list(smallbox.find_all('a'))[3])['href']
# 				comments='https://news.ycombinator.com/'+str(gtlnkkcoments)
# 				print(comments)
# 			except IndexError:
# 				print("NOOO")

		
	
def news():
	for hi in range(1,3):	
		url='https://news.ycombinator.com/news?p='+str(hi)
		Soup=BeautifulSoup(requests.get(url).text,'lxml')
		Brain=Soup.find_all(class_='athing')
		Footer=Soup.find_all('td',class_='subtext')
		head=[]
		ul=[]
		yr=[]
		top=[]	
		cntcoment=[]	
		lnkcoment=[]	
		for smallbox in Footer: 
			scores=smallbox.find('span',class_='score')
			Number=scores.text if scores else "No data Found"	
			Point=Number				
			agess=smallbox.find('span',class_='age')
			ages=agess.text
			top.append(Point)
			yr.append(ages)
			try:
				countcomments=(list(smallbox.find_all('a'))[3])
				nocomment=countcomments.text.replace(' ',' ') if countcomments else "No data Found"
				gtlnkkcoments=(list(smallbox.find_all('a'))[3])['href']
				comments='https://news.ycombinator.com/'+str(gtlnkkcoments)
				cntcoment.append(nocomment)
				lnkcoment.append(comments)
				
			except IndexError :("No, any record found")
						
		for Box in Brain:
			Titles=Box.find('a',class_='titlelink').text
			links=Box.find('a',class_='titlelink')['href']	
			head.append(Titles)
			ul.append(links)		
		
		Rate='\n'.join(top)
		Title='\n'.join(head)
		link='\n'.join(ul)
		ccmt='\n'.join(lnkcoment)
		lnkcmt='\n'.join(cntcoment)
		age='\n'.join(yr)
		

		# print(f'Title:{Title} lnkcmtLinks:{link} Points:{Rate} comments:{ccmt} linkscomment:{lnkcmt} age:{age}')

		with open('haha.csv',newline='',mode='a+') as fire:
			spam=csv.writer(fire,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			spam.writerow([Title,link])


news()
