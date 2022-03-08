# Hello World!

print('Hello World!')
print()
# see https://www.python-ds.com/python-3-escape-sequences
# \n -- to set a new line
print('Sample text with line break')
print('\nline1\nline2\nline3')
print()
# \' -- to put a single quote
print('Sample text \'Hello World\'')
print()
# \r -- carrige return ... it does not work as expected -- to clarify ?
print('Hello World \r12345')
print()
# \t -- to tab
print('Hello\tWorld')
print()
# \b -- to enter Backspace... not sure if it works correctly -- to clarify ? 
print('Hello\bWorld')
print()
# \f -- to set form feed... not sure ... -- to clarify ?
print('Hello\fWorld')
print()
# \ooo -- to set Octal Value -- a sample from internet ... 
print('\110\145\154\154\157\40\127\157\162\154\144\41')
print()
# \xhh -- to set Hex Value -- a sample from internet ... 
print('\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21')
print()
# how to print '\'
print('Hello\\World!')
print()


# multiple arguments
print('Hello','World','!')
print()

print('My name is Phyton.')
print('Monty Phyton')
print()

print('My name is Phyton.', end=' ')
print('Monty Phyton')
print()

print('My','name','is','Phyton.', end=' ', sep='-')
print('Monty','Phyton',sep='_')
print()

print('My name is Phyton.', sep='-', end=' ')
print('Monty Phyton')
print()


# HOME WORK 2.1

print('\n----------------\nHOME WORK 2.1\n----------------\n')

print('Programming***Essentials***in...Python')

print('Programming','Essentials','in',sep='***',end='...')
print('Python')
print()


# HOME WORK 2.2

print('\n----------------\nHOME WORK 2.2\n----------------\n')

print('    *    ')
print('   * *   ')
print('  *   *  ')
print(' *     * ')
print('***   ***')
print('  *   *  ')
print('  *****  ')

print('\n')
print('    *    ','   * *   ','  *   *  ',' *     * ','***   ***','  *   *  ','  *****  ',sep='\n')

print('\n')
print('   ',' * ','   ',sep=' ')
print('   ','* *','   ',sep='*')
print('  *','   ','*  ',sep='*')
print(' * ','   ',' * ',sep='*')
print('***','   ','***',sep='*')
print('  *','   ','*  ',sep='*')
print('  *','***','*  ',sep='*')

print('\n')
print('    *    \n   * *   \n  *   *  \n *     * \n***   ***\n  *   *  \n  *****  \n' * 2)

print('\n')
print('    *    '*2,'   * *   '*2,'  *   *  '*2,' *     * '*2,'***   ***'*2,'  *   *  '*2,'  *****  '*2,sep='\n')

print('\n')
print(' '*4,      ' '*4,sep='*')
print(' '*3,' '*1,' '*3,sep='*')
print(' '*2,' '*3,' '*2,sep='*')
print(' '*1,' '*5,' '*1,sep='*')
print('*'*2,' '*3,'*'*2,sep='*')
print(' '*2,' '*3,' '*2,sep='*')
print(' '*2,'*'*3,' '*2,sep='*')

print('\n')
print(' '*4,'*'*1,' '*4,sep='*'*1)
print(' '*3,' '*1,' '*3,sep='*'*2)
print(' '*2,' '*3,' '*2,sep='*'*2)
print(' '*1,' '*5,' '*1,sep='*'*2)
print('*'*2,' '*3,'*'*2,sep='*'*2)
print(' '*2,' '*3,' '*2,sep='*'*2)
print(' '*2,'*'*3,' '*2,sep='*'*2)


# HOME WORK 2.3

print('\n----------------\nHOME WORK 2.3\n----------------\n')

print('"I\'m"','"\"learning\""','"\"\"Python\"\""',sep='\n')



# HOME WORK 2.4

print('\n----------------\nHOME WORK 2.4\n----------------\n')

john = 1
mary = 2
adam = 3

print('Jonh = ' + str(john), 'Mary = ' + str(mary), 'Adam = ' + str(adam), sep=', ', end='.')

total_apples = john + mary + adam

print('\nTotal apples = ', total_apples)


# HOME WORK 2.5

print('\n----------------\nHOME WORK 2.5\n----------------\n')

kilometers_out = 0
miles_out = 0
k = 1.61

kilometers_in = round(float(input('Enter distance in kilometers = ')),2)
miles_in      = round(float(input('Enter distance in miles = ')),2)

kilometers_out = round(miles_in * k,2)
miles_out = round(kilometers_in / k,2)

print()
print(kilometers_in ,'kilometers =', miles_out, 'miles')
print(miles_in ,'miles =', kilometers_out, 'kilometers')
print ('\nBye')



# HOME WORK 2.6

print('\n----------------\nHOME WORK 2.6\n----------------\n')


x = 0
y = 0

x = float(input('Enter X = '))

y = (3 * x**3) - (2 * x**2) + (3 * x) - 1

print()
print('X =', x, 'Y =', y)
print ('\nBye')


# HOME WORK 2.7

print('\n----------------\nHOME WORK 2.7\n----------------\n')

#this program computes the number of seconds in a given number of hours

a = 0 #number of hours
seconds = 3600 #number of seconds in 1 hour

a = int(input('Enter the number of hours = '))

print('Hours:',a) #print the number of hours
print('Seconds in Hours:', a * seconds) #print the number of seconds  
print ('\nBye')




# HOME WORK 2.8

print('\n----------------\nHOME WORK 2.8\n----------------\n')

print('Simple Calculator')
x = 0 #1st operand
y = 0 #2nd operand
operation = '+' #operation
z = 0 #result

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
    z = 'null'

print()
print('X =', x)
print('Y =', y)
print('Operation:', operation)
print('Result (Z) =', z)
print ('\nBye')



# HOME WORK 2.9

print('\n----------------\nHOME WORK 2.9\n----------------\n')

x = 0 #input
y = 0 #output

x = float(input('Enter X: '))

y =  1 / (x + 1/(x + 1/(x + 1/x)))

print()
print('X =', x)
print('Y =', y)
print ('\nBye')



# HOME WORK 2.10

print('\n----------------\nHOME WORK 2.10\n----------------\n')

print('Hello World again!')



# HOME WORK 2.11

print('\n----------------\nHOME WORK 2.11\n----------------\n')

a = 11111
b = 1111111
print(a * b)


# HOME WORK 2.12

print('\n----------------\nHOME WORK 2.12\n----------------\n')

a = 42
b = 4
c = 2

# d = a / (b + c *(-c))

e = b + c *(-c)

if not(e == 0):
    d = a / e
else:
    d = 'undefiined'    
    
print(d)



# HOME WORK 2.13

print('\n----------------\nHOME WORK 2.13\n----------------\n')

a = 2014
b = 14
print(a **b)


# HOME WORK 2.14

print('\n----------------\nHOME WORK 2.14\n----------------\n')

#this program computes the number of seconds in a given number of hours

a = 1 #number of days
seconds = 3600 #number of seconds in 1 hour
hours = 24 #humber of hours in 1 day

a = int(input('Enter the number of days = '))

print('Days:',a) #print the number of days
print('Seconds in Days:', a * hours * seconds) #print the number of seconds  
print ('\nBye')



# HOME WORK 2.15

print('\n----------------\nHOME WORK 2.15\n----------------\n')

a = 2014.0
b = 14
print(a **b)



print('\n----------------\nHOME WORK COMPLETED\n----------------\n')
dumy_str = input('Enter anything to exit')



