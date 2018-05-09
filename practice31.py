def print_max(int1,int2,int3):
    max=0

    if int1>int2:
        max=int1
    else:
        max=int2
        
    if max>int3:
        max=max
    else:
        max=int3

    return max

a=int(input("첫 번째 정수를 입력하세요:"))
b=int(input("두 번째 정수를 입력하세요:"))
c=int(input("세 번째 정수를 입력하세요:"))

d=print_max(a,b,c)

print("가장 큰 정수 :",d)

