i=1
num=1
while i <=3:
    j=1
    while j<=5:
        if num%3==0:
            print('*',end=' ')
        else:
            print(num,end=' ')
        num = num+1
        j=j+1
    print(end='\n')
    i=i+1

