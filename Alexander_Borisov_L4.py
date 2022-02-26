# HOME WORK 4.1

print('\n----------------\nHOME WORK 4.1\n----------------\n')

print('CALCULATOR. Version with functions defined in program')

# my variables

calc_type = '' #calculator type
operation = '' #operation / function
x = 0 #1st operand / list of values
y = 0 #2nd operand

# my functions

# simple math operations
def my_operations (operation, x, y):
    
    z = 0

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
            z = None
    else:
        print('***ERROR*** Unknown math operation:', operation)
        z = None

    print('\n', x, operation, y, '=', z)

# some math functions
def my_functions (operation, x):

    z = 0
    
    if operation == 'min':
        z = min(x)
    elif operation == 'max':
        z = max(x)
    else:
        return

    print('\n', operation, 'of', x, 'is', z)   

# my main program

while calc_type.upper() != 'E':

    calc_type = input('\nEnter: O-Operations, F-Functions or E-Exit')

    if calc_type.upper() == 'O':
        #simple operations
        print('Simple operations:  + , - , *, /, **, %, // ')
        x = float(input('Enter 1-st operand (X): '))
        y = float(input('Enter 2-nd operand (Y): '))
        operation = input('Enter operation ( + , - , *, /, **, %, // ): ')
        my_operations(operation, x, y) #call my function to run math OPERATION
 
    elif calc_type.upper() == 'F':
        #functions
        print('Functions:  min(), max()')
        operation = input('Enter function ( min, max ):')
        if operation in ('min', 'max'):
            x = input('Enter a space separated list of values:').split()
            my_functions(operation, x) #call my function to run math FUNCTION
        else:
            print('***ERROR*** Unknown function:', operation)

    elif calc_type.upper() == 'E':
        pass

    else:
        print('\nUnknown calculator type, re-enter')
else:
    print('\nBye')



# HOME WORK 4.2

print('\n----------------\nHOME WORK 4.2\n----------------\n')

print('Detect LEAP YEAR program ')

# my variables
start_year = 1582
end_year = 9999
list_years = []
i = 0

# my functions
def is_year_leap(yr):

    if (yr % 4 == 0) and (yr % 100) != 0:
        return True
    elif yr % 100 == 0 and (yr / 100) % 4 == 0:
        return True
    else:
        return False

# my program
list_years = input('Enter a space separated list of Years:').split()

for i in range (len(list_years)):

    if int(list_years[i]) in range(start_year, end_year+1):
        if is_year_leap(int(list_years[i])):
            print('Year', list_years[i], 'is a leap year')
        else:
            print('Year', list_years[i], 'is a common year')
    else:
        print('Year', list_years[i], 'is out of range (1582 - 9999)')



# HOME WORK 4.3

print('\n----------------\nHOME WORK 4.3\n----------------\n')

print('DAYS in YEAR/MONTH program ')

# my variables
start_year = 1582
end_year = 9999
year_month_days = [31,28,31,30,31,30,31,31,30,31,30,31] #days on default

curr_year = 2000
curr_month = 12
days_in_month = 31

# my functions
def is_year_leap(yr):

    if (yr % 4 == 0) and (yr % 100) != 0:
        return True
    elif yr % 100 == 0 and (yr / 100) % 4 == 0:
        return True
    else:
        return False

# my program
curr_year = int(input('Enter YEAR (yyyy):'))
curr_month = int(input('Enter MONTH (mm):'))

if curr_year in range(start_year, end_year+1):
    if is_year_leap(curr_year) and (curr_month == 2):
        days_in_month = year_month_days[curr_month-1] + 1
    else:    
        days_in_month = year_month_days[curr_month-1]
    print('DAYS in Month:', days_in_month)
else:
    print('Year', curr_year, 'is out of range (1582 - 9999)')     
        


# HOME WORK 4.4

print('\n----------------\nHOME WORK 4.4\n----------------\n')

print('DAY of the YEAR program ')

# my variables
start_year = 1582
end_year = 9999

curr_date = []
curr_year = curr_month = curr_day = 0
i = 0
day_of_year = 0


# my functions
def is_year_leap(year):

    if (year % 4 == 0) and (year % 100) != 0:
        return True
    elif year % 100 == 0 and (year / 100) % 4 == 0:
        return True
    else:
        return False

def days_in_month(year, month):

    year_month_days = [31,28,31,30,31,30,31,31,30,31,30,31] #days on default
    days = 0

    if is_year_leap(year) and (month == 2):
        days = year_month_days[month-1] + 1
    else:    
        days = year_month_days[month-1]
    return days

# my program
curr_date = input('Enter DATE (yyyy-mm-dd):').split('-')
curr_year = int(curr_date[0])
curr_month = int(curr_date[1])
curr_day = int(curr_date[2])

if (curr_year in range(start_year, end_year+1) #check if input DATE is valid 
    and curr_month in range(1,13)
    and curr_day <= days_in_month(curr_year, curr_month) ):

    for i in range(1,13):
        if (i < curr_month):
            day_of_year = day_of_year + days_in_month(curr_year, i)
        elif (i == curr_month):
            day_of_year = day_of_year + curr_day
        else:
            exit
    print('DAY of the Year:', day_of_year)
else:
    print('***ERROR*** Incorrect input DATE')     



# HOME WORK 4.5

print('\n----------------\nHOME WORK 4.5\n----------------\n')


print('If Number is PRIME program ')

# my variables

num = []
i = 0

# my functions

def is_prine(num):

    for i in range (2,num):
        if (num % i == 0):
            return False
    return True

# my program

num = input('Enter a space separated sequence of numbers (>1):').split()
print(num)

for i in range(len(num)):
    if is_prine(int(num[i])):
        print(num[i], 'is PRIME')
    else:
       print(num[i], 'is not prime' )



# HOME WORK 4.6

print('\n----------------\nHOME WORK 4.6\n----------------\n')


print('CONVERTOR liters/100km into miles/gallons')

# my variables

calc_type = '' #calculator type
l = m = 0

# my functions

def liters_100km_to_miles_gallon(l):

    mile_to_km = 1.609344
    gallon_to_liter = 3.785411784
    m = 0

    m = round( ( 1 / (l/gallon_to_liter/100 * mile_to_km) ), 2) 
    print(l, 'liters_100km is equal to', m, 'miles/gallons')  

def miles_gallon_to_liters_100km(m):

    mile_to_km = 1.609344
    gallon_to_liter = 3.785411784
    l = 0

    l = round (100 / (m * mile_to_km/gallon_to_liter), 2)
    print(m, 'miles/gallons is equal to', l, 'liters_100km') 


# my program

while calc_type.upper() != 'E':

    calc_type = input('\nEnter input data: L-liters/100km, M-miles/gallons or E-Exit')

    if calc_type.upper() == 'L':
        l = float(input('Enter liters/100km: '))
        liters_100km_to_miles_gallon(l)
    elif calc_type.upper() == 'M':
        m = float(input('Enter miles/gallons: '))
        miles_gallon_to_liters_100km(m)
    elif calc_type.upper() == 'E':
        pass
    else:
        print('\nUnknown convertor type, re-enter')    

else:
    print('\nBye')






           
