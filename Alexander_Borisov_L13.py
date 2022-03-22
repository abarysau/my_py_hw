# HOME WORK 13

print('\n----------------\nHOME WORK 13\n----------------\n')

print('PIZZERIA sample program v3\n')

# my external modyles

import json

# my objects & variables


class PizzaError(ValueError):
    def __init__(self, text='PizzaError'):
        ValueError.__init__(self)
        self.__mytext = text
    def __str__(self):
        return 'PizzaError: '+ self.__mytext
    
class Pizza_menu_item:
    def __init__(self, pizza_name, pizza_size):
        self.pizza_name = pizza_name
        self.pizza_size = pizza_size


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

    def remove_pizza_from_menu(self, pizza_name):
        for i in range (len(self.__pizza_list)):
            if pizza_name == self.__pizza_list[i][0]:
                del self.__pizza_list[i]
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

    def unload_menu_to_file(self, file):
        for i in range (len(self.__pizza_list)):
            item = Pizza_menu_item(self.__pizza_list[i][0], self.__pizza_list[i][1])
            item_json = json.dumps(item, default=encode_menu_item)
            print(item_json)
            file.writelines(str(item_json) + '\r\n')
        print('The menu was unloaded in JSON format') 

    def load_menu_from_file(self, file):
        self.__pizza_list = []
        for line in file:
            item_json = line.rstrip('\r\n')
            if item_json != '':
                print(item_json)
                item = json.loads(item_json, object_hook=decode_menu_item)
                self.__pizza_list.append((item.pizza_name, item.pizza_size))
        print('The menu was reloaded from JSON file')         
    
my_pizza = Pizza()
n = i = 0
input_str = ''
my_list = []
pizza = ''
size = ''
file_name = ''


# my functions

def print_pizza_menu(menu_list):

    print('\nPizza menu:\n')
    for i in range(len(menu_list)):
        print(menu_list[i][0].capitalize(),
              'is available in size = ' + str(menu_list[i][1]),
              sep='\t')


def encode_menu_item(item):
    if isinstance (item, Pizza_menu_item):
        return item.__dict__
    else:
        raise TypeError(item.__class__.__name__ + 'is not JSON serelizable') 

def decode_menu_item(item):
    return Pizza_menu_item(item['pizza_name'], item['pizza_size'])


# my program

print_pizza_menu(my_pizza.pizza_list())


# Part 1: Work with PIZZA menu
input_str = input('\nWould you like to change pizza menu? (Y/N):')

while (input_str.upper() == 'Y'):
    input_str = input('\nEnter: A-Add pizza, C-Change pizza size, R-Remove pizza, \n \
      U-Unload menu, L-Load menu or E-Exit:')
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
    elif input_str.upper() == 'R':
        pizza = input('\nEnter Pizza name to remove:').strip().lower()
        if my_pizza.remove_pizza_from_menu(pizza):
            print('Pizza = ', pizza, 'was removed from menu')

    elif input_str.upper() in ('U','L'):
        try:
            file_name = ''
            file_name = input('\nEnter the file name (pizza.json): ')
            if (file_name == ''):
                file_name = 'pizza.json'
            if input_str.upper() == 'U':
                output_file = open(file_name, 'w')
                my_pizza.unload_menu_to_file(output_file)
                output_file.close()
            elif input_str.upper() == 'L':
                input_file = open(file_name, 'r')
                my_pizza.load_menu_from_file(input_file)
                input_file.close()
                
        except PizzaError as pe:
            print(pe)
        except Exception as e:
            print(e)                

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
