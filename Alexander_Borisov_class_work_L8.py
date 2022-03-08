# CLASS WORK FOR LECTION 8

print('\n----------------\nCLASS WORK 8\n----------------\n')

print('SORT sample program with TRY/EXCEPT')

n = i = 0
my_list = []
type_of_sort = ''

# my functions

def my_sort(L,srt_type):

    Sort_f = True
    i = n = 0

    if not (srt_type.lower() in ('increased','decreased','reversed')):
        raise ValueError('***Incorrect arg "srt_type" for function "my_sort"')

    while (Sort_f == True) and (srt_type.lower() in ('increased','decreased')):

        Sort_f = False
        n = len(L)
        for i in range(n-1):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                Sort_f = True
    else:
         if srt_type.lower() in ('decreased','reversed'):
             L.reverse()
         return L

# my program

while not(n > 0):
    try:
        n = int(input('Enter how many elements do u want: (n > 0):'))
        assert n > 0
    except ValueError:
        print('***Incorrect input. A number is expected. Re-enter, please')
    except:
        print('***Incorrect input. A number > 0 is expected. Re-enter, please')
else:
    print('Ok, the list will contain', n, 'elements')

for i in range(n):
    my_list.append(input('Enter next element:'))
    
print('Ok, the list contains the following:', my_list)
type_of_sort = input('Enter type of sort ("increased" / "reversed" / "decreased"):')

print('Sort Method =', type_of_sort)
try:
    my_list = my_sort(my_list,type_of_sort)
    print('Ok, the sorted list is:', my_list)
except ValueError:
    print('***Unknown Sort Method =', type_of_sort)
except:
    print('***Unknow error in my_sort')

print('\nBye')

