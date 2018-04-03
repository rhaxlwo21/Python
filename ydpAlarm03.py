#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

def remove_tag(content):
   cleanr =re.compile('<.*?>','[ 중식 ]')
   cleantext = re.sub(cleanr, '', content)
   return cleantext

page_url = 'http://www.ydp.hs.kr/index.do'
res = requests.get(page_url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')

#print(soup)
#출력


index_mlsv_box = soup.find('div',{'cl ass' : 'index_mlsv_box'})

#print(index_mlsv_box)

schoolFood = soup.find_all("h4")
print(schoolFood)
