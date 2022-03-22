# HOME WORK 8.2

print('\n----------------\nHOME WORK 8.2\n----------------\n')

print('TIMER sample program\n')

# my objects & variables

class Timer:
    def __init__(self):
        print('Hello from Timer!')
        self.__mytime = (0,0,0)

    def __str__(self):
        return ('Time = ' + str(self.__mytime[0]).rjust(2,'0')
                    + ':' + str(self.__mytime[1]).rjust(2,'0')
                    + ':' + str(self.__mytime[2]).rjust(2,'0') )
              
    def set(self, hh, mm, ss):
        self.__mytime = (hh, mm, ss)

    def reset(self):
        self.__mytime = (0, 0, 0)

    def next_second(self):
        self.__seconds = (self.__mytime[0] * 3600 +
                          self.__mytime[1] * 60 +
                          self.__mytime[2] )
        
        self.__seconds +=1 # add one second
        
        if (self.__seconds >= 86400):
            self.__seconds -=86400

        self.__hh = self.__seconds // 3600
        self.__mm = (self.__seconds - self.__hh * 3600) // 60
        self.__ss = self.__seconds - self.__hh * 3600 - self.__mm * 60
        self.__mytime = (self.__hh, self.__mm, self.__ss)

    def prev_second(self):
        self.__seconds = (self.__mytime[0] * 3600 +
                          self.__mytime[1] * 60 +
                          self.__mytime[2] )
        
        self.__seconds -=1 # subtract one second
        
        if (self.__seconds < 0):
            self.__seconds +=86400

        self.__hh = self.__seconds // 3600
        self.__mm = (self.__seconds - self.__hh * 3600) // 60
        self.__ss = self.__seconds - self.__hh * 3600 - self.__mm * 60
        self.__mytime = (self.__hh, self.__mm, self.__ss)
        

my_timer = Timer()
n = i = 0
input_str = ''
hh = mm = ss = 0

# my functions


# my program

while (input_str.upper() != 'N'):
    while True:
        input_str = input('Enter TIME (HH:MM:SS) ')
        try:
            hh = int(input_str[0:2])
            mm = int(input_str[3:5])
            ss = int(input_str[6:8])
            assert (    (hh >= 0 and hh <= 23)
                    and (mm >= 0 and mm <= 59)
                    and (ss >= 0 and ss <= 59) )
            break
        except ValueError:
            print('***Incorrect input. Time in format HH:MM:SS is expected')
        except:
            print('***Incorrect input. The TIME value is out of range')

    my_timer.set(hh, mm, ss)
    print(my_timer)

    while (input_str.upper() != 'STOP'):
        input_str = input('Enter command NEXT, PREV or STOP ')
        if input_str.upper() == 'NEXT':
            print('next_second()')
            my_timer.next_second()
        elif input_str.upper() == 'PREV':
            print('prev_second()')
            my_timer.prev_second()
        else:
            pass
        print(my_timer)
    
    input_str = input('\nWould you like to continue with other TIME? (Y/N):')


print('\nBye')
