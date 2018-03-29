# 정수를 입력받아 양수,0,음수 구별하기
# 연속 if문 사용

num=int(input("점수를 입력하세요:"))

if num>90:
    print("A 입니다.")
elif num<=89 and num>=80:
    print("B 입니다.")
elif num<=79 and num>=70:
    print("C 입니다.")
elif num<=69 and num>=60:
    print("D 입니다.")
else:
    print("E 입니다.")
