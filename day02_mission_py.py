# day02_mission
# mission_01

import random

secret = random.randint(1,10)
# 1<= secret <=10 randint함수 랜덤한 정수(int) 반환
guess = random.randint(1,10)
if secret > guess :
    print ('too low')
elif secret < guess :
    print ('too high')
elif secret ==guess :
    print ('just right')



