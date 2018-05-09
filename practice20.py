#반복문을 통해 덧셈값을 증가시키며 summ에 덧셈값을 누적

count = 1   #덧셈을 시작할 값 1
summ = 0    #덧셈값을 누적해서 더할 변수

#while count <=10:
for count in range(1,11,1):
    summ = summ + count
    count= count + 1

print("합계는",summ)
