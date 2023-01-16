#ex. 6-1

for k in[3,2,1,0]:
    print(k)


#ex. 5-1
# m으로 시작하는 대문자로 만들어보자


#ex. 5-4
letter = '''    Dear {salutation} {name},\n
    Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room}, especially near any {animals}.True
  
    Send us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.
    \n
    Thank you for your support.
    Sincerely, 
    {spokesman}
    {job_title}'''
print(letter)
#ex 5-5.

letter = '''    Dear {salutation} {name},\n
    Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room}, especially near any {animals}.True

    Send us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.
    \n
    Thank you for your support.
    Sincerely, 
    {spokesman}
    {job_title}'''

salutation = 'my friend'
name = 'Rora'
product = 'vacuum cleaner'
verbed = 'hit hard'
room = 'room101'
animals = 'any companion animals'
amount = 'cost'
percent = '95'
spokesman = 'Casey'
job_title = 'manager'
print(f'''Dear {salutation} {name},\n
    Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room}, especially near any {animals}.True

    Send us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.
    \n
    Thank you for your support.
    Sincerely, 
    {spokesman}
    {job_title} ''')

#ex 5-6(f'이용'

print('''Dear {salutation} {name},\n
    Thank you for your letter. We are sorry that our {product} {verbed} in your {room}. Please note that it should never be used in a {room}, especially near any {animals}.True

    Send us your receipt and {amount} for shipping and handling. We will send you another {product} that, in our tests, is {percent}% less likely to have {verbed}.
    \n
    Thank you for your support.
    Sincerely, 
    {spokesman}
    {job_title} '''.format(salutation = 'my friend',
name = 'Rora',
product = 'vacuum cleaner',
verbed = 'hit hard',
room = 'room101',
animals = 'any companion animals',
amount = 'cost',
percent = '95',
spokesman = 'Casey',
job_title = 'manager'))


#ex 5-6.



