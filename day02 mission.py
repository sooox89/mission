# day02_mission
# mission_01

import random

secret = random.randint(1, 10)
# 1<= secret <=10
# randint 함수 랜덤한 정수(int) 반환
guess = random.randint(1, 10)
if secret > guess:
    print('too low')
elif secret < guess:
    print('too high')
elif secret == guess:
    print('just right')

# mission_02

small = True
green = True
if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")
