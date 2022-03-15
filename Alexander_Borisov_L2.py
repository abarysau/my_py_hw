# HOME WORK 3.1

print('\n----------------\nHOME WORK 3.1\n----------------\n')

n1 = n2 = n3 = n4 = 0
max_value = 0
max_number = ' '

print('Enter 4 numbers (N1, N2, N3, N4)...')

# set 1-st number as max
n1 = float(input('N1 = '))
max_value = n1
max_number = 'N1'

# replace if any of next numbers is bigger
n2 = float(input('N2 = '))
if n2 > max_value:
    max_value = n2
    max_number = 'N2'

n3 = float(input('N3 = '))
if n3 > max_value:
    max_value = n3
    max_number = 'N3'    

n4 = float(input('N4 = '))
if n4 > max_value:
    max_value = n4
    max_number = 'N4'    

print('Max number is', max_number, '=', max_value) 



# HOME WORK 3.2

print('\n----------------\nHOME WORK 3.2\n----------------\n')

n1 = n2 = n3 = n4 = n5 = n6 = 0
max_value = 0
min_value = 0

print('Enter 6 integer numbers (N1...N6)')

# enter all numbers
n1 = int(input('N1 = '))
n2 = int(input('N2 = '))
n3 = int(input('N3 = '))
n4 = int(input('N4 = '))
n5 = int(input('N5 = '))
n6 = int(input('N6 = '))

# get max/min values
max_value = max(n1, n2, n3, n4, n5, n6)
min_value = min(n1, n2, n3, n4, n5, n6)

print('Max value is', max_value) 
print('Min value is', min_value) 



# HOME WORK 3.3

print('\n----------------\nHOME WORK 3.3\n----------------\n')

plant = ' '
wanted_plant = 'Spathiphyllum'

# ask for a plant name
plant = input('Enter a plant name:')
plant = plant.strip()

# check the name and its first letter
if plant.upper() == wanted_plant.upper():
    if plant[0].isupper() and plant[1:].islower():
        print ('Yes -', plant, 'is the best plant ever!')
    else:
        print('No, I want a big', wanted_plant)
else:
    print('I want', wanted_plant, 'Not', plant)



# HOME WORK 3.4

print('\n----------------\nHOME WORK 3.4\n----------------\n')

attempt_count = 1
income = tax = 0
tax_rate = 15

print('You have 5 attempts to calculate Tax')
while attempt_count <= 5:
    print('Attempt', attempt_count)
    income = float(input('Enter Income ='))
    tax = round(income / 100 * tax_rate)
    print('Income=',income, 'Tax rate(%)=', tax_rate, 'Rounded Tax=',tax)
    attempt_count +=1
    
    

# HOME WORK 3.5

print('\n----------------\nHOME WORK 3.5\n----------------\n')

start_year = 1582
end_year = 9999
curr_year = 2000

print('It will determine the kind (common / leap) of year')
curr_year = int(input('Enter Year ='))

if curr_year in range(start_year, end_year) :
    if (curr_year % 4 == 0) and (curr_year % 100) != 0:
        print('Year', curr_year, 'is a leap year')
    elif curr_year % 100 == 0 and (curr_year / 100) % 4 == 0:
        print('Year', curr_year, 'is a leap year')
    else:
        print('Year', curr_year, 'is a common year')
else:
    print('Year', curr_year, 'is out of range (1582 - 9999)')     



# HOME WORK 3.6

print('\n----------------\nHOME WORK 3.6\n----------------\n')

magic_number = 978
number = 0

print('Guess the magic number (or enter -1 to escape)')

while (number != -1) and (number != magic_number): 
    number = int(input('Enter a number ='))
    if number == magic_number:
        print('Well done, muggle! You are free')
    elif number == -1:
        print('Ok, Bye')
    else:
        print("Ha ha! You're stuck in my loop!")



# HOME WORK 3.7

print('\n----------------\nHOME WORK 3.7\n----------------\n')

import time
i = k = 0

print('Mississippi counter')
k = int(input('Enter number of iterations ='))
k +=1

for i in range(1, k):
    time.sleep(1)
    print(i, 'Mississippi')

print('Ready or not, here I come!')



# HOME WORK 3.8

print('\n----------------\nHOME WORK 3.8\n----------------\n')

print('Guess the secret exit word (hint: "chupacabra")')

while True:
    if input('Enter a word =') == 'chupacabra':
        break

print("You've successfully left the loop")



# HOME WORK 3.9

print('\n----------------\nHOME WORK 3.9\n----------------\n')

user_word = ''
l = i = 0

print('Vowel Eater. it will remove the vowels from the entered word')

user_word = input('Enter a word:').upper()
l = len(user_word)

for i in range(0,l):
    if user_word[i] in ('A', 'E', 'I', 'O', 'U'):
        continue
    print(user_word[i])



# HOME WORK 3.10

print('\n----------------\nHOME WORK 3.10\n----------------\n')

user_word = ''
result_str = ''
l = i = 0

print('Vowel Eater 2. it will remove the vowels from the entered word')

user_word = input('Enter a word:').upper()
l = len(user_word)

for i in range(0,l):
    if user_word[i] in ('A', 'E', 'I', 'O', 'U'):
        continue
    result_str += user_word[i]

print(result_str)



# HOME WORK 3.11

print('\n----------------\nHOME WORK 3.11\n----------------\n')

c0 = 0
step = 0

print('Task "Lothar Collatz"')

# get a number 
while not (c0 > 1):
    c0 = int(input('Enter a number:'))
    if c0 < 2:
        print('Incorrect number. It should be > 1. Retype, please')

#evaluate the number
while c0 != 1:
    if c0 % 2 == 0:
        #even number
        c0 = c0 / 2 
    else:
        #odd number
        c0 = c0 * 3 + 1
    print(int(c0))
    step +=1
        
print('Steps =', step)



# HOME WORK 3.12

print('\n----------------\nHOME WORK 3.12\n----------------\n')

print('My Calculator')

operation = '' #operation / function
x = 0 #1st operand / list of values
y = 0 #2nd operand
z = 0 #result

calc_type = input('Enter calc. type: 1 - operations, 2 - functions ')

if calc_type == '1':
    #simple operations
    print('Simple operations:  + , - , *, /, **, %, // ')
    x = float(input('Enter 1-st operand (X): '))
    y = float(input('Enter 2-nd operand (Y): '))
    operation = input('Enter operation ( + , - , *, /, **, %, // ): ')

    if operation == '+':
        z = x + y
    elif operation == '-':
        z = x - y
    elif operation == '*':
        z = x * y
    elif operation == '**':
        z = x **y
    elif operation == '%':
        z = x % y
    elif (operation == '/' or operation == '//'):
        if (not (y == 0) and operation == '/'):
            z = x / y
        if (not (y == 0) and operation == '//'):
            z = x // y
        if y == 0:
            print('***ERROR*** Incorrect 2nd operand (Y):', y)
            z = 'null'
    else:
        print('***ERROR*** Unknown operation:', operation)
        z = None
    print('\nResult (Z) =', z)

elif calc_type == '2':
    #functions
    print('Functions:  min(), max()')
    operation = input('Enter function ( min, max ):')
    if operation in ('min', 'max'):
        x = input('Enter list of values:').split()
    if operation == 'min':
        z = min(x)
    elif operation == 'max':
        z = max(x)
    else:
        print('***ERROR*** Unknown operation:', operation)
        z = None
    print('\nResult =', z)   

else:
    print('\nUnknown calculator, bye')



# HOME WORK 3.13

print('\n----------------\nHOME WORK 3.13\n----------------\n')

print('Set 2nd bit to 1')

SetB = int('10',2)

bits = int(input('Enter a binary value:'),2)

print('\nInput value')
print('Bin=', bin(bits), 'Dec=', bits)

bits = bits | SetB

print('\nUpdated Input value')
print('Bin=', bin(bits), 'Dec=', bits)



# HOME WORK 3.14

print('\n----------------\nHOME WORK 3.14\n----------------\n')

print('Reset the 2nd and 3rd bits to "0" if it is set to "1"')

SetB2 = int('0010',2)
SetB3 = int('0100',2)

bits = int(input('Enter a binary value:'),2)

print('\nInput value')
print('Bin=', bin(bits), 'Dec=', bits)


if bits & SetB2 != 0:
    print('Bit 2 to reset')
    bits = bits ^ SetB2

if bits & SetB3 != 0:
    print('Bit 3 to reset')
    bits = bits ^ SetB3

print('\nUpdated Input value')
print('Bin=', bin(bits), 'Dec=', bits)



print('\n----------------\nHOME WORK COMPLETED\n----------------\n')
dumy_str = input('Enter anything to exit')




