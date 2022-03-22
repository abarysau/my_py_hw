# HOME WORK 8.1

print('\n----------------\nHOME WORK 8.1\n----------------\n')

print('STACK sample program\n')

# my objects & variables

class Stack:
    def __init__(self):
        print('Hello from Stack!')
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        if len(self.__stack_list) > 0:
            self.__stack_last_val = self.__stack_list[-1]
            del self.__stack_list[-1]
            return self.__stack_last_val
        else:
            return None

class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__stack_push_counter = 0
        self.__stack_pop_counter = 0
    
    def push(self, val):
        Stack.push(self, val)
        self.__stack_push_counter +=1

    def pop(self):
        self.__stack_last_val = Stack.pop(self)
        if not(self.__stack_last_val == None): 
            self.__stack_pop_counter +=1
        return self.__stack_last_val

    def push_counter(self, val):
        if val.lower() == 'reset':
            self.__stack_push_counter = 0
        elif val.lower() == 'get':
            return self.__stack_push_counter
        else:
            return None      

    def pop_counter(self, val):
        if val.lower() == 'reset':
            self.__stack_pop_counter = 0
        elif val.lower() == 'get':
            return self.__stack_pop_counter
        else:
            return None      

Stack_object = CountingStack()
n = i = 0
input_str = ''
my_list = []

# my functions


# my program

input_str = input('Put a string of elements separated by space:')
print('Input string:',input_str)
my_list = input_str.split()
print('Input list:', my_list)

n = len(my_list)
for i in range(n):
    Stack_object.push(my_list[i]) # push input elements into STACK

print('Input elements were loaded into STACK')

input_str = input('\nWould you like to get elements from STACK? (Y/N):')

while True:
    if input_str.upper() == 'Y':
        print(Stack_object.pop()) # pop next element from STACK
        input_str = input('Get other element (Y/N):') 
    else:
        break

print('\n')
print('Total PUSH operations:',Stack_object.push_counter('get'))
print('Total successful POP operations:',Stack_object.pop_counter('get'))

print('\nBye')
