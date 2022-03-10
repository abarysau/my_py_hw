# HOME WORK 9.2

print('\n----------------\nHOME WORK 9.2\n----------------\n')

print('PIZZERIA sample program\n')

# my objects & variables


class PizzaError(ValueError):
    def __init__(self, text='PizzaError'):
        ValueError.__init__(self)
        self.__mytext = text
    def __str__(self):
        return 'PizzaError: '+ self.__mytext
    
class Pizza:
    def __init__(self):
        print('Hello from Pizza!')
        self.__pizza_list = [('margherita',['small', 'medium','big']),
                             ('marinara'  ,['small',          'big']),
                             ('carbonara' ,[         'medium'      ])]

    def pizza_list(self):
        return self.__pizza_list

    def add_pizza_to_menu(self, pizza_name, available_size):
        for i in range (len(self.__pizza_list)):
            if pizza_name == self.__pizza_list[i][0]:
                raise PizzaError('Pizza already in list')
        self.__pizza_list.append((pizza_name, available_size))
        return True
                
    def change_pizza_size_in_menu(self, pizza_name, available_size):
        for i in range (len(self.__pizza_list)):
            if pizza_name == self.__pizza_list[i][0]:
                self.__pizza_list[i] = (pizza_name, available_size)
                return True
        raise PizzaError('Pizza not exists in list')       

    def make_pizza(self, pizza_name, pizza_size):
        for i in range (len(self.__pizza_list)):
            if pizza_name == self.__pizza_list[i][0]:
                if pizza_size in self.__pizza_list[i][1]:
                    return True
                else:
                    raise PizzaError('Pizza is not available in this size')
        raise PizzaError('Pizza not exists')
                

my_pizza = Pizza()
n = i = 0
input_str = ''
my_list = []
pizza = ''
size = ''

# my functions

def print_pizza_menu(menu_list):

    print('\nPizza menu:\n')
    for i in range(len(menu_list)):
        print(menu_list[i][0].capitalize(),
              'is available in size = ' + str(menu_list[i][1]),
              sep='\t')


# my program

print_pizza_menu(my_pizza.pizza_list())


# Part 1: Work with PIZZA menu
input_str = input('\nWould you like to change pizza menu? (Y/N):')

while (input_str.upper() == 'Y'):
    input_str = input('\nEnter: A-Add pizza, C-Change pizza size or E-Exit:')
    if input_str.upper() in ('A','C'):
        pizza = input('\nEnter Pizza name:').strip().lower()
        size = input('\nEnter available pizza sizes separated by space:').lower().split()
        try: 
            if input_str.upper() == 'A':
                if my_pizza.add_pizza_to_menu(pizza, size):
                    print('Pizza = ', pizza, 'in size = ', size, 'was added to menu')
            if input_str.upper() == 'C':
                if  my_pizza.change_pizza_size_in_menu(pizza, size):
                    print('Pizza = ', pizza, 'in size = ', size, 'was changed in menu')
        except PizzaError as pe:
            print(pe)
    elif input_str.upper() == 'E':
        break
    else:
        pass
    input_str = input('\nWould you like to make other changes in pizza menu? (Y/N):')
    if input_str.upper() == 'N': 
        print_pizza_menu(my_pizza.pizza_list())


# Part 2: Order PIZZA from menu    
input_str = input('\nWould you like to order a pizza from menu? (Y/N):')

while input_str.upper() == 'Y':

    input_str = input('\nEnter Pizza/size from menu:')

    try:
        my_list = input_str.split('/')
        pizza = my_list[0].strip().lower()
        size = my_list[1].strip().lower()
        print('OK, You ordered pizza', pizza.upper(), 'in size', size.upper())

        if my_pizza.make_pizza(pizza, size):
            print('Your order will be available soon. Enjoy!')

    except IndexError:
        print('Use "/" to separate PIZZA / SIZE')

    except PizzaError as pe:
        print(pe)
        
    input_str = input('\nWould you like to get other pizza? (Y/N):')
    if not (input_str.upper() == 'Y'):
        break


print('\nBye')
