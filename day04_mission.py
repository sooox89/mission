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
#things = [things.capitalize() for things in things]
things[-2] = things[-2].title()
print(things)
# ex 7-6.
#things = [things.upper() for things in things]
things = ["mozzarella","cinderella", "salmonella"]
things[0]=things[0].upper()
print(things)
# ex 7-7.
things = ["mozzarella","cinderella", "salmonella"]
del things[-1]
print(things)
# ex 7-8.
surprise = ["Groucho","Chico","Harpo"]
print(surprise)
# ex 7-9.
surprise[-1] = "harpo"
surprise[-1] = surprise[-1][::-1]
print(surprise)
# ex 7-10.
a_list = [number for number in range(10) if number % 2 == 0]
print(a_list)
# ex 7-11.
start1 = ["fee","fie","foe"]

rhymes = [("flop","get a mop"),
          ("fope","turn the rope"),
          ("fa","get your ma"),
          ("fudge","call the judge"),
          ("fat","pet the cat"),
          ("fog","walk the dog"),
          ("fun","say we're done"),
          ]

start2 = "Someone better"

start1 = [start1.capitalize()+"!" for start1 in start1 ]

start1 = ','.join(start1)
r = [r[0].capitalize()+"!" for r in rhymes]
r = ','.join(r)



# for sstart1,rhymes1,sstart2,rhymes2 in zip(start1,rhymes,start2,rhymes)
#     print()



