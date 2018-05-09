import random

randomNum1 = random.randint(20,40)
randomNum2 = random.randint(20,40)

if randomNum1>randomNum2:
    temp = randomNum2
    randomNum2 = randomNum1
    randomNum1 = temp

for i in range(randomNum1+1,randomNum2,1):
    print(i)
