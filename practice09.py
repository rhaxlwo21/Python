# 사용자에게 값을 입력받고 random을 사용하여 입력받은 수를 비교하여 출력

import random

coin=int(input("1~10사이에서 하나를 고르세요:"))

rCoin=random.randrange(10)+1

if rCoin==coin:
    print("일치합니다")
else:
    print("일치하지 않습니다. 답은",rCoin,"입니다")
