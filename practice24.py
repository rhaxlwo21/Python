#for i in range(1,6):
#    print(i,end=' ')

i=1
while i <= 4:
    j=1
    if i%2==1:
        num = 1
        while j<= 4:
            print(num,end=' ')
            num = num + 1
            j= j+1
    else:
        num = 4
        while j <= 4:
            print(num,end=' ')
            num = num -1
            j=j+1
    print(end='\n')
    i=i+1
