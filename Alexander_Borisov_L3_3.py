# HOME WORK 3.3

print('\n----------------\nHOME WORK 3.3\n----------------\n')

print('SORT sample program')

n = i = 0
my_list = []
type_of_sort = ''

# my functions

def my_sort(L):

    Sort_f = True
    i = n = 0
    
    while Sort_f == True:

        Sort_f = False
        n = len(L)
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                Sort_f = True
    else:
         return L

# my program

n = int(input('Enter how many numbers do u want: (n > 0):'))
for i in range(n):
    my_list.append(int(input('Enter next number:'))) 

print('Ok, the list contains the following:', my_list)
type_of_sort = input('Enter type of sort ("increased" / "reversed" / "decreased"):')

if type_of_sort == 'increased':
    print('Sort Method =', type_of_sort)
#    my_list.sort()
    my_list = my_sort(my_list)
elif type_of_sort == 'reversed':
    print('Sort Method =', type_of_sort)
    my_list.reverse()
elif type_of_sort == 'decreased':
    print('Sort Method =', type_of_sort)
#    my_list.sort()
    my_list = my_sort(my_list)
    my_list.reverse()
else:
    print('Unknown Sort Method =', type_of_sort)

print('Ok, the sorted list:', my_list)
