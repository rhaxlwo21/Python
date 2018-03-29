#나이가 10살이상이고,그리고 키가 165이상이면 놀이기구를 탈 수 있다.

age=int(input("나이를 입력하세요:"))
height=int(input("키를 입력하세요:"))

if age>=10 and height>=165:
    print("놀이기구를 탈 수 있습니다.")
else:
    print("놀이기구를 이용하실수 없습니다.")
