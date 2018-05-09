i=1
while i<=3:
    j=1
    while j<=7:
        if ((j==3 or j==6) and i==1) or ((j==2 or j==5) and i==2) or ((j==1 or j==4 or j==7) and i==3): 
            print('#',end=' ')
        else:
            print('*',end=' ')
        j+=1
    print(end='\n')
    i+=1
