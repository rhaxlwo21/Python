#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

page_url = 'http://www.ydp.hs.kr/index.do'
res = requests.get(page_url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')

#print(soup)
#출력


index_mlsv_box = soup.find('div',{'class' : 'index_mlsv_box'})

print(index_mlsv_box)
