#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

page_url = 'http://www.ydp.hs.kr/index.do'
res = requests.get(page_url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')

#print(soup)
#출력


data = soup.find('div',{'cl ass' : 'index_mlsv_box'})

#print(data)

schoolFood = soup.find_all("h4")
print(schoolFood)
