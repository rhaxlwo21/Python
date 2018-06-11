from bs4 import BeautifulSoup               #HTML 문서의 태그 분석
import pandas as pd                             #데이터 분석
from urllib.request import urlopen      #정보를 받아오는 역할
import urllib
import numpy as np

url_base = "http://movie.naver.com/"
url_sub = "movie/sdb/rank/rmovie.nhn?sel=cur&data=20180406"

#urlopen 메소드는 괄호안의 주소의 내용을 읽어 가져온다.
page = urlopen(url_base + url_sub)

#BeautifulSoup를 사용해서 urlopen으로 가져온 내용을 태그별로 정리한다.
soup = BeautifulSoup(page, "html.parser")
#print(soup)
#print(soup.find_all('div',"tit5"))

#string 속성을 이용하면 태그를 제외하고 문자열만 추출할 수 있다.
#print(soup.find_all('div','tit5')[0].a.string)
#print(soup.find_all('td','point')[0].string)

#find_all로 찾은 결과가 여러개인 경우, 그리고 모두 저장하고 싶을때
#movie_name = [soup.find_all('div', 'tit5')[n].a.string for n in range(0,30)]
#print(movie_name)
#movie_point = [soup.find_all('td', 'point')[n].string for n in range(0,30)]
#print(movie_point)

date = pd.date_range('2018-4-6' , periods=10, freq='D')
#print(date)

movie_date=[]
movie_name=[]
movie_point=[]

for today in date:
    html = url_base + "movie/sdb/rank/rmovie.nhn?sel=cur&date={date}"
    response = urlopen(html.format(date=urllib.parse.quote(today.strftime('%Y%m%d'))))
    soup = BeautifulSoup(response, "html.parser")
    
    end = len(soup.find_all('td', 'point'))

    movie_date.extend([today for n in range(0,end)])
    movie_name.extend([soup.find_all('div', 'tit5')[n].a.string for n in range(0,end)])
    movie_point.extend([soup.find_all('td', 'point')[n].string for n in range(0,end)])

#print(movie_date[0], movie_name[0], movie_point[0])

movie = pd.DataFrame({'data' : movie_date, 'name' : movie_name, 'point' : movie_point})
print(movie.head())

print(movie.info())

movie['point'] = movie['point'].astype(float)

movie_unique = pd.pivot_table(movie, index=['name'], aggfunc=np.sum)
movie_best = movie_unique.sort_values(by='point', ascending=False)
print(movie_best.head(10))
print(movie_best.tail(10))
