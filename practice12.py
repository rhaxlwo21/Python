import random

time=random.randint(1,24) #1~24사이 난수
sunny=random.choice([True,False]) #참, 거짓중 하나
print(time)

if sunny:
    print("현재 날씨가 화창합니다.")
else:
    print("현재 날씨가 화창하지 않습니다.")

if ((time>=6 and time<=9) or (time>=14 and time <=16)) and sunny:
    print("종달새가 노래를 한다.")
else:
    print("종달새가 노래를 하지 않는다.")
