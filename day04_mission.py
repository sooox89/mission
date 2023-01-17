# ch7 list & tuple
# ex 7-1.
import random
birth = random.randint(1980,2011)   ##임의로 출생년도 1980~2010만 ..
years_list = [ birth for birth in range(birth,birth+6)]
print(years_list)

# ex 7-2.
print(years_list[2])
# ex 7-3.
print(years_list[-1])
# ex 7-4.
things = ["mozzarella","cinderella", "salmonella"]
print(things)
# ex 7-5. 리스트 컴프리헨션 [x.capitalize() for x in original_list]
things = [things.capitalize() for things in things]
print(things)

