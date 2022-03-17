# HOME WORK 10.1

print('\n----------------\nHOME WORK 10.1\n----------------\n')


print('\nHistogram sample program \n')


# my classes & variables

file_name = ''
input_str =''
counters = {}
myhist = []
i = n = ch = 0

# my functions


# my program


# get data from a TXT file

while True:
    try:
        file_name = input('\nEnter TXT file name: ')
        input_file = open(file_name, 'r')
        break
    except FileNotFoundError:
        print('No such file or directory, re-enter, please')
    
for line in input_file:
    print(line.rstrip('\n\r'))
    input_str += line.rstrip().lower()
input_file.close()

# make a dictionary with all possible letters
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

# for each letter count entries in input file  
for i in range (len(input_str)):     
    n = counters.get(input_str[i])
    if (n != None) :
        counters.update({input_str[i]:n+1})

# keep only the letters with entries > 0
for ch in range(ord('a'), ord('z') + 1):  
    n = counters.get(chr(ch))
    if (n == 0):
        counters.pop(chr(ch))

# print the histogram
myhist = list(counters.items())
for i in range(len(myhist)):
    print(myhist[i][0], '->',myhist[i][1] )


print('\nBye')
