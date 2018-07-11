from bs4 import BeautifulSoup
from urllib.request import urlopen
from tkinter import *

def getWebData():
    url_base = 'http://www.sunrint.hs.kr/'
    url_syb = 'index.do#none'
    page = urlopen(url_base+url_syb)
    
    soup = BeautifulSoup(page,'html.parser')
    meal = soup.find('p','menu').get_text()
    meal = meal.strip()
    lblMealText['text'] = meal

window = Tk()
window.title('급식조아 ~')
window.geometry('500x250+100+100')
lblMenuText = Label(window,  text='오늘의 메뉴는?')
lblMealText = Label(window, text='---')
btnGetData = Button(window, text='메뉴 확인', command=getWebData)

lblMenuText.pack()
lblMealText.pack()
btnGetData.pack()
