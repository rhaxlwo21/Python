int1 = int(input("0~100사이의 정수를 입력하세요:"))

if int1>=90:
    print("수")
if int1>=80 and int1<90:
    print("우")
if int1>=70 and int1<80:
    print("미")
if int1>=60 and int1<70:
    print("양")
if int1>=50 and int1<60:
    print("가")
if int1>100 or int1<=0:
    print("error")
