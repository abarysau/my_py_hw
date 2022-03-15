# HOME WORK 10.3

print('\n----------------\nHOME WORK 10.3\n----------------\n')


print('\nSTUDENT DATA sample program\n')


# my classes & variables

class StudentDataException(Exception):
    def __init__(self, message=''):
        super().__init__(self)
        self.my_message = message
    def __str__(self):
        return str((self.my_message))

class BadLine(StudentDataException):
    def __init__(self, line, message='Bad data in line'):
        super().__init__(self)
        self.line = line
        self.my_message = message
    def __str__(self):
        return str((self.line, self.my_message))
    
class FileEmpty(StudentDataException):
    def __init__(self, file_name, message='The file is empty'):
        super().__init__(self)
        self.file_name = file_name
        self.my_message = message
    def __str__(self):
        return str((self.file_name, self.my_message))
        
        

file_name = ''
input_str =''
input_list = []
students = {}
students_list = []

i = n  = 0

# my functions

def check_student_data(L):

    if (len(L) != 3):
        return False
    
    if not L[2].replace('.','0').isdecimal():
        return False

    return True


# my program


# get data from a TXT file

while True:
    try:
        file_name = input('\nEnter the student data file name: ')
        input_file = open(file_name, 'r')
        break
    except FileNotFoundError:
        print('No such file or directory, re-enter, please')

print('\nThe file contains the following:\n')     
for line in input_file:
    print(line.rstrip('\n\r'))
    input_str = line.strip()
    input_list = input_str.lower().split()

    # formal check
    if not check_student_data(input_list): 
        raise BadLine(input_str)

    # for each student get the sum of the student's points
    student_name = input_list[0] + ' ' + input_list[1]
    n = students.setdefault(student_name.title(), float(0))
    students.update({student_name.title():n + float(input_list[2])})
        
    
input_file.close()

# print the student list with total points collected
if (len(students) == 0):
    raise FileEmpty(file_name)
else:
    print('\nThe students get the following total points:\n')
    students = dict(sorted(students.items(), key=lambda item: item[0]))
    students_list = list(students.items())
    
    for i in range(len(students_list)):
        print(students_list[i][0], students_list[i][1], sep='\t')   

print('\nBye')
