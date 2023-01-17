# ch7 list & tuple
# ex 7-1.
import random
birth = random.randint(1980,2011)   ##임의로 출생년도 1980~2010만 ..
year_lists = [ birth for birth in range(birth,birth+6)]
print(year_lists)

