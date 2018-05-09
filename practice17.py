#정수를 입력받아 팩토리얼(!) 구하

n = int(input("정수를 입력하세요:"))

fact = 1
for i in range(1,n+1):
    fact = fact * i

print(n,"! 은",fact,"이다")
