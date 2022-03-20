# HOME WORK 7.1

print('\n----------------\nHOME WORK 7.1\n----------------\n')


print('\nMy SPLIT program\n')

# my modules

# from packages.mysplit.mysplit import mysplit
from packages.mysplit import mysplit

# my variables

my_str = ''
my_list =[]

# my program

while True:

    my_str = input('\nEnter a string of elements separated by spaces:\n')

    # my_list = mysplit(my_str)
    my_list = mysplit.mysplit(my_str)

    print('\nThe following list was created:')
    print(my_list)

    my_str = input('\nWould you like to continue? (Y/N):')
    if my_str.upper() == 'N':
        break

print('\nBye')    




           
