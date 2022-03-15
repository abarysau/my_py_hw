# HOME WORK 10.2

print('\n----------------\nHOME WORK 10.2\n----------------\n')


print('\nHistogram sample program. Ver 2 \n')


# my classes & variables

file_name = ''
input_str =''
output_str =''
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

print('\nThe TXT file contains the following text:\n')     
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

# sort dictionary, print the histogram and save it into a TXT file
counters = dict(sorted(counters.items(), key=lambda item: item[1], reverse=True))
myhist = list(counters.items())

file_name = file_name.lower().rstrip('.txt') + '.hist.txt'
output_file = open(file_name, 'w')

print('\nThe following histogram was created:\n')
for i in range(len(myhist)):
    output_str = str(myhist[i][0]) + ' -> ' + str(myhist[i][1])
    print(output_str)
    output_file.writelines(output_str + '\n')

output_file.close()
print('\nFile', file_name, 'was saved')

print('\nBye')
