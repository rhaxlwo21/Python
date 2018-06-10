from bs4 import BeautifulSoup
import requests

page_url = 'http://www.ydp.hs.kr/index.do'
res = requests.get(page_url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')

#print(soup)
#출력

get = ""
data = soup.find('div',{'class' : 'text_contents'})
total = data.find("a")
get += str(total)
#print(get)


#getFile = open("D:\\totalOpen.txt","a")
#getFile.write(get)
#rmChar = '<a href="/72059/subMenu.do">[ 중식 ]<br/><br/>1021kcal</a>'
#getFile.close()
get1 = get.replace('<a href="/72059/subMenu.do">',"")
get2 = get1.replace('[ 중식 ]<br/>',"")
get3 = get2.replace('<br/>1011 kcal',"")
get4 = get3.replace('</a>',"")

print(get4)
#index_board_mlsv_031_271980 > div > div.text_contents > a
