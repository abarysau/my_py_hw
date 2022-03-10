# HOME WORK 9.3

print('\n----------------\nHOME WORK 9.3\n----------------\n')

print('WEEKER sample program\n')

# my objects & variables


class WeekerError(ValueError):
    def __init__(self, text='WeekerError'):
        ValueError.__init__(self)
        self.__mytext = text
    def __str__(self):
        return 'WeekerError: '+ self.__mytext
    
class Weeker:
    def __init__(self, day = 'MON'):
        print('Hello from Weeker!')
        self.__week_days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        self.__curr_day = day.upper()
        self.__curr_day_no = 0
        for i in range(len(self.__week_days)):
            if self.__week_days[i] == self.__curr_day:
                self.__curr_day_no = i+1
        if self.__curr_day_no == 0:
            raise WeekerError('Unknown day of week')    

    def __str__(self):
        return self.__curr_day

    def week_list(self):
        return self.__week_days

    def add_days(self, days):
        n = self.__curr_day_no + days
        if (n > 7) or (n < -7): 
            n = n - (n // 7) * 7
        elif (n > 0) and (n <= 7):
            pass
        elif (n == 0):
            n = 7
        elif (n < 0) and (n >= -7):    
            n = n + 7
        else:
            pass
        self.__curr_day_no = n
        self.__curr_day = self.__week_days[n-1] 
        return self.__curr_day
                
                

my_day = Weeker()
n = i = 0
input_str = ''


# my functions

# my program

print(my_day.week_list())

while True:

    input_str = input('\nEnter a day from the list above:')
    try:
        my_day = Weeker(input_str.strip()) # set a day of week to play with
        print(my_day)
    except WeekerError as we:
        print(we)
        print('Sorry, I cannot serve your request!')
        break      

    while True:
        try:
            n = int(input('\nEnter +/- number of days to add/subtract:'))
            my_day.add_days(n) # add/subtract days 
            print(my_day)      # print new day
            input_str = input('\nWould you like to check other offset? (Y/N):')
            if input_str.upper() == 'N':
                break
        except ValueError as ve:
            print (ve)

    input_str = input('\nWould you like to set other day? (Y/N):')
    if input_str.upper() == 'N':
        break


print('\nBye')
