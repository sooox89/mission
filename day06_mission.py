#ch9 ex 9-1

list_hp = ['Harry', 'Ron', 'Hermione']
def good(list):
    return list
result = good(list_hp)
print(result)

#ch9 ex 9-2

# def get_odds(number):
#     for number in range(1,11):
#         yield number % 2 == 1
#         number += 1
# result = get_odds(1)
# print(result)

def get_odds(number):
    for number in range(1,10,2):
        yield number

odds = get_odds(1)
for x in odds :
    print(x)

