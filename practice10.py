# 랜덤으로 값을 입력받아 동전의 앞뒷면을 출력한다.

import turtle
import random

screen=turtle.Screen() # 이미지를 사용하기 위해 사용

image1="d:\\front.jpg"
image2="d:\\rear.jpg"

screen.addshape(image1) # 이미지를 스크린에 추가
screen.addshape(image2) # 이미지를 스크린에 추가

t1 = turtle.Turte()
coin = random.randint(0,1) #0부터 1까지 범위의 난수

if coin == 0:
    t1.shape(image1)
    t1.stamp()
else:
    t1.shape(image2)
    t1.stamp()
