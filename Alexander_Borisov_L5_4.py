# HOME WORK 5.2

print('\n----------------\nHOME WORK 5.2\n----------------\n')


print('\n"To do list" programm \n')


import time

# my variables

oper_type = ''
my_activity = ''
my_list = []
my_list_str = []
file_name = ''
i = n = 0

# my functions


# my program

while oper_type.upper() != 'E':
    
    oper_type = input('\nEnter: O-Open, N-New or E-exit')

    if oper_type.upper() == 'O':
 
        while True:
            file_name = input('\n Enter file name to open (or E-Exit): ')
            if file_name.upper() == 'E':
                break
            fin = open(file_name, 'r')
            print('\n---------------------------------------')
            print('To DO List from file:', file_name)
            print('---------------------------------------\n')   
            for line in fin:
                print(line.rstrip('\r\n'))          
            fin.close()
            break

    elif oper_type.upper() == 'N':
        curr_date = time.localtime()
        my_activity_date = '{}-{:{fill}2}-{:{fill}2}'.format(curr_date.tm_year,
                                                             curr_date.tm_mon,
                                                             curr_date.tm_mday,
                                                             fill='0') 
        while True:
            my_activity = input('Enter Activity (or S-stop): ')
            if my_activity.upper() == 'S':
                break
            my_activity_time = input('Enter time HH-MM ')
            my_list.append([my_activity_date, my_activity_time, my_activity]) 

        print('\n---------------------------------------')
        print('To DO List for', time.asctime(curr_date))
        print('---------------------------------------\n')
        for i in range(len(my_list)):
              my_list_str.append('\t'.join(my_list[i]))  
              print(my_list_str[i])
        print('---------------------------------------')

        while True:
            file_name = input('\n To save enter file name (or E-Exit): ')
            if file_name.upper() == 'E':
                break
            fout = open(file_name, 'w')
            for i in range(len(my_list_str)):
                fout.writelines(my_list_str[i]+'\r\n')
            fout.close()
            print('File', file_name, 'was saved')
            break
            
    elif oper_type.upper() == 'E':
        pass    

    else:
        print('\nUnknown command, re-enter')
else:
    print('\nBye')
