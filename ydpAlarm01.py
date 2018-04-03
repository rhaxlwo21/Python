import urllib2



url="http://news.naver.com/"

temp=urllib2.urlopen(url)

f=open("news.txt","w")

f.write(temp.read())

f.close()

temp.close()
