# HOME WORK 9.1

print('\n----------------\nHOME WORK 9.1\n----------------\n')

print('QUEUE sample program\n')

# my objects & variables


class QueueError(ValueError):
    def __init__(self, text='QueueError'):
        ValueError.__init__(self)
        self.__mytext = text
    def __str__(self):
        return 'QueueError: '+ self.__mytext
    
class Queue:
    def __init__(self):
        print('Hello from Queue!')
        self.__queue_list = []

    def put(self, val):
        self.__queue_list.insert(0, val)

    def get(self):
        if len(self.__queue_list) > 0:
            self.__queue_last_val = self.__queue_list[-1]
            del self.__queue_list[-1]
            return self.__queue_last_val
        else:
            raise QueueError('no more elements in the queue')


Queue_object = Queue()
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
    Queue_object.put(my_list[i]) # insert input elements into QUEUE

print('Input elements were put into QUEUE')

input_str = input('\nWould you like to get elements from QUEUE? (Y/N):')

while True:
    if input_str.upper() == 'Y':
        try:
            print(Queue_object.get()) # get next element from QUEUE
        except QueueError as qe:
            print(qe)
        input_str = input('Get other element (Y/N):') 
    else:
        break

print('\nBye')
