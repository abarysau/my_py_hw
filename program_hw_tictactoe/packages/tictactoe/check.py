# Module Check. Functions to use in tictactoe

print('\nModule tictactoe check is used \n')

def is_line_filled(Lines,n):
    # it checks if exists a line with 'n':    
    # 0 - line is completed 
    # 1 - line is about filled (2 from 3)
    # 2 - only one field is filled
    i = 0
    for i in range(len(Lines)):
        if len(Lines[i]) == n:
             return True
    return False    
