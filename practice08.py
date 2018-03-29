# 동전 던지기 게임
# import random과 random.randrange(2)를 이용하여 0과1을 랜덤으로 나오게 설정

import random

print("동전 던지기 게임을 시작합니다.")
coin=random.randrange(2)
if coin == 0:
    print("앞면입니다")
else:
    print("뒷면입니다.")
print("게임이 종료되었습니다.")
