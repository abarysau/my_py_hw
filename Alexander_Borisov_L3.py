# HOME WORK 3.1

print('\n----------------\nHOME WORK 3.1\n----------------\n')

print('Program to work with list elements')

hat_list = [1, 2, 3, 4, 5]
len_list = 0
i = 0 #index

print('in the following following list', hat_list)
len_list = len(hat_list)
i = len_list // 2

print('replace element #', i)
hat_list[i] = int(input('Enter a new element value (integer):'))

print('Updated list', hat_list, 'contains', len_list, 'elements')

del hat_list[len_list - 1]

print('The list with removed last element:', hat_list)



# HOME WORK 3.2

print('\n----------------\nHOME WORK 3.2\n----------------\n')

print('Program to work with THE BEATLES')

Beatles = []
print('\nThe group currently contains', len(Beatles), 'members')
Beatles.append(input('Help us to create the band. Enter #1 (John Lennon):'))
print('\nThe group currently contains', len(Beatles), 'members')

Beatles.append(input('Enter #2 (Paul McCartney ):'))
Beatles.append(input('Enter #3 (George Harrison ):'))
print('\nThe group contains', len(Beatles), 'members.', 'They are', Beatles)

print('\nAdd #4 (Stu Sutcliffe) and #5 (Pete Best)')
for i in range (2):
    Beatles.append(input('Enter #' + str(len(Beatles)+1) + ':'))

print('\nThe group contains', len(Beatles), 'members.', 'They are', Beatles)

print('\nRemove members who left the Group')
member_died = input('Enter member who has died (Stu Sutcliffe):')
if (member_died in Beatles):
    Beatles.remove(member_died)
else:
    print('*** probably typo, we will remove', Beatles[3]) 
    Beatles.pop(3)
print('Now the group contains', Beatles)

print('\nWe will delete the last member #5 who left the group -', Beatles[-1])
del Beatles[-1]

Beatles.insert(0, input('Insert a new drummer (Ringo Starr):'))

print('\nThe famous band contained', Beatles)



# HOME WORK 3.3

print('\n----------------\nHOME WORK 3.3\n----------------\n')

print('SORT sample program')

n = i = 0
my_list = []
type_of_sort = ''

n = int(input('Enter how many numbers do u want: (n > 0):'))
for i in range(n):
    my_list.append(int(input('Enter next number:'))) 

print('Ok, the list contains the following:', my_list)
type_of_sort = input('Enter type of sort ("increased" / "reversed" / "decreased"):')

if type_of_sort == 'increased':
    print('Sort Method =', type_of_sort)
    my_list.sort()
elif type_of_sort == 'reversed':
    print('Sort Method =', type_of_sort)
    my_list.reverse()
elif type_of_sort == 'decreased':
    print('Sort Method =', type_of_sort)
    my_list.sort()
    my_list.reverse()
else:
    print('Unknown Sort Method =', type_of_sort)

print('Ok, the sorted list:', my_list)



# HOME WORK 3.4

print('\n----------------\nHOME WORK 3.4\n----------------\n')

print('Program to remove duplicates in list')

n = i = 0
my_list = []
new_list = []

# create a list
n = int(input('Enter how many numbers do u want: (n > 0):'))
for i in range(n):
    my_list.append(int(input('Enter next number:'))) 
print('Ok, the list contains the following:', my_list)

# sort the list
my_list.sort()

# remove duplicates
for i in range(n):
    if (len(new_list) == 0):
        new_list.append(my_list[i])
    elif (my_list[i] != new_list[-1]):
        new_list.append(my_list[i])

# print output
print('The list with unique elements only:', new_list)



# HOME WORK 3.5

print('\n----------------\nHOME WORK 3.5\n----------------\n')

print('SPLIT / SUM program sample')

n = i = 0
input_str = ''
my_list = []
my_list_num = []
Z = 0

# get a list

input_str = input('Put a string of numbers by space:')
print('Input string:',input_str)
my_list = input_str.split()
print('Input list:', my_list)

# convert to integer

n = len(my_list)
for i in range(n):
    my_list_num.append(int(my_list[i]))
print('Input list of numbers:', my_list_num)

# get the SUM of list

Z = sum(my_list_num)
print('The SUM of the list is :', Z)



# HOME WORK 3.6

print('\n----------------\nHOME WORK 3.6\n----------------\n')

print('Program to identify duplicates in list')

n = i = 0
my_list = []
new_list = []

# create a list
n = int(input('Enter how many numbers do u want: (n > 0):'))
for i in range(n):
    my_list.append(int(input('Enter next number:'))) 
print('Ok, the list contains the following:', my_list)

# sort the list
my_list.sort()

# identify duplicates
for i in range(n):
    if (len(my_list) > 1):
        if (my_list[i] == my_list[i-1]):
            if (len(new_list) == 0):
                new_list.append(my_list[i])
            elif (my_list[i] != new_list[-1]):
                new_list.append(my_list[i])

# print output
print('The list of duplicate values', new_list)



# HOME WORK 3.7

print('\n----------------\nHOME WORK 3.7\n----------------\n')

print('Program to calculate AVERAGE sample')

n = i = 0
input_str = ''
my_list = []
my_list_num = []
Z = 0

# get a list

input_str = input('Put a string of numbers by space:')
print('Input string:',input_str)
my_list = input_str.split()
print('Input list:', my_list)

# convert to integer

n = len(my_list)
for i in range(n):
    my_list_num.append(int(my_list[i]))
print('Input list of numbers:', my_list_num)

# get the AVERAGE of list

if len(my_list) > 0:
    Z = sum(my_list_num) / len(my_list)

print('The AVERAGE value of the list is :', Z)



# HOME WORK 3.8

print('\n----------------\nHOME WORK 3.8\n----------------\n')

print('Program to calculate the arithmetic mean')

a = b = 0
i = 0
my_list = []
Z = 0

# get input data
a = int(input('Enter left border a:'))
b = int(input('Enter right border b:'))

if (a <= b):
    # create the list of numbers
    print('Input numbers to process:')
    for i in range (a, b+1):
        if (i % 3 == 0):
            my_list.append(i)
    print(my_list)
    # get the arithmetic mean
    if len(my_list) > 0:
        Z = sum(my_list) / len(my_list)
    print('The arithmetic mean:',Z)     
else:
    print('*** incorrect input: a <= b is expected')







      






           
