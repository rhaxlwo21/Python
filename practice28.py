maxX=int(input("가로크기:"))
maxY=int(input("세로 크기:"))
i=1

while i<=maxY:
    j=1
    while j<=maxX:
        if i==1 or i==maxY or j==1 or j==maxX:
            print('#',end=' ')
        else:
            print('*',end=' ')
        j+=1
    print(end='\n')
    i+=1

