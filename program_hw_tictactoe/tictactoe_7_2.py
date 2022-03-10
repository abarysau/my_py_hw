# HOME WORK 7.2

print('\n----------------\nHOME WORK 7.2\n----------------\n')


print('\nКрестики - Нолики 7.2\n')

# my modules

from random import randrange
from packages.tictactoe.check import is_line_filled

# my variables

Field = ['1','2','3','4','5','6','7','8','9']
Free_Field = ['1','2','3','4','5','6','7','8','9']
field_num = ' '
User_Lines = [['1','2','3'],
              ['4','5','6'],
              ['7','8','9'],
              ['1','4','7'],
              ['2','5','8'],
              ['3','6','9'],
              ['1','5','9'],
              ['3','5','7']]
Comp_Lines = [['1','2','3'],
              ['4','5','6'],
              ['7','8','9'],
              ['1','4','7'],
              ['2','5','8'],
              ['3','6','9'],
              ['1','5','9'],
              ['3','5','7']]

# my functions

def print_field(F):
    # print the game field
    print(F[0],'|',F[1],'|',F[2])
    print('-','-','-','-','-')
    print(F[3],'|',F[4],'|',F[5])
    print('-','-','-','-','-')
    print(F[6],'|',F[7],'|',F[8])

def fill_line(Lines, field_num):
    # remove a free field from all possible lines:
    # if a line has no free field then it is completed
    i=0
    for i in range(len(Lines)):
        if len(Lines[i]) >= 1:
            if field_num in Lines[i]:
                Lines[i].remove(field_num)

def delete_line(Lines, field_num):
    # delete all lines with specified field:
    # a player cannot complete a line if other player got any field there 
    i=0
    n = len(Lines)
    for i in range(n):
        if len(Lines[n-i-1]) >= 1:
            if field_num in Lines[n-i-1]:
                Lines.pop(n-i-1)

def get_free_field(F):
    # return any free field
    if '5' in F:
        return '5'
    else:
        # return F[len(F) // 2]
        return F[randrange(len(F))]

# the function below is migrated to module packages.tictactoe.check

#def is_line_filled(Lines,n):
#    # it checks if exists a line with 'n':    
#    # 0 - line is completed 
#    # 1 - line is about filled (2 from 3)
#    # 2 - only one field is filled
#    i = 0
#    for i in range(len(Lines)):
#        if len(Lines[i]) == n:
#             return True
#    return False    

def get_line_filled(Lines,n):
    # it returns a line filled in specific ways 'n'     
    i = 0
    for i in range(len(Lines)):
        if len(Lines[i]) == n:
             return Lines[i]
    return []        


# my program

while field_num.upper() != 'E':

    print_field(Field)
    field_num = input('\nEnter Field Number(1-9) or E-Exit')

    if field_num in Free_Field:
        
        Field[int(field_num)-1] = 'X'
        Free_Field.remove(field_num)
        fill_line(User_Lines,field_num)
        delete_line(Comp_Lines,field_num)

        if is_line_filled(User_Lines,0):
            print_field(Field)
            input('Congatulation, You won!')
            break                    

        if len(Free_Field) > 0:
            if is_line_filled(Comp_Lines,1):
                # try to complete my line
                field_num = get_free_field(get_line_filled(Comp_Lines,1))
            elif is_line_filled(User_Lines,1):
                # avoid possible player's line completion
                field_num = get_free_field(get_line_filled(User_Lines,1))
            elif is_line_filled(Comp_Lines,2):
                # try to continue any of my line
                field_num = get_free_field(get_line_filled(Comp_Lines,2))
            else:
                # get any free field
                field_num = get_free_field(Free_Field)

            Field[int(field_num)-1] = 'O'
            Free_Field.remove(field_num)
            fill_line(Comp_Lines,field_num)
            delete_line(User_Lines,field_num)

            if is_line_filled(Comp_Lines,0):
                print_field(Field)
                input('Sorry, Computer won!')
                break
        else:
            print('No free fields anymore')
            break
    elif field_num.upper() == 'E':
        pass
    else:
        print('\n***Field number', field_num, 'is not free or incorrect, re-enter\n')    
else:
    print('\nBye')





           
