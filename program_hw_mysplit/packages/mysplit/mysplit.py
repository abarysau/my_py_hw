# Module "mysplit". Functions to work with strings

print('\nModule MYSPLIT is used\n')

def mysplit(S):

    # it gets S - string
    # it returns L - list of elements from S
    
    next_element = ''
    L = []
    i = n = 0

    n = len(S)
    for i in range(n):
        if S[i] != ' ':
            next_element += S[i] # build element: add next char
        if ((S[i] == ' ') or (i == n-1)) and (next_element != ''):
            L.append(next_element) # add next completed element to the list
            next_element = ''
    return L




           
