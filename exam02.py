n = int(input("4자리 숫자를 입력하세요:"))
num1=0
num2=0
num3=0
num4=0
num = 0

num1=n%10
n=n//10

num2=n%10
n=n//10

num3=n%10
n=n//10

num4=n%10

if num1==num4 and num2==num3:
    print("거꾸로 읽어도 같습니다.")
else:
    print("거꾸로 읽으면 다릅니다.")
