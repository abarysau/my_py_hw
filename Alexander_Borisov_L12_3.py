# HOME WORK 12.3

print('\n----------------\nHOME WORK 12.3\n----------------\n')


print('\nPhone Contacts sample program\n')

# my modules

import csv

# my classes & variables

class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return str(self.name).ljust(20) + ' ' + str(self.phone)
        
class Phone():
    def __init__(self):
        self.contacts = []

    def __str__(self):
        self.contacts_str = ''
        for i in range(len(self.contacts)):
            self.contacts_str = self.contacts_str + str(self.contacts[i]) + '\n'
        return str(self.contacts_str)

    def load_contacts_from_csv(self, file):
        with open(file, newline='') as csvfile:
            fieldnames = ['Name', 'Phone']
            reader = csv.DictReader(csvfile, fieldnames)
            for row in reader:
                self.contacts.append(PhoneContact(row['Name'],row['Phone']))

    def remove_contact(self, name):
        for i in range (len(self.contacts)):
            if name == self.contacts[i].name:
                del self.contacts[i]
                print('The contact was removed')
                return True
        return False   

    def add_contact(self, name, number):
        contact_exists = 'N'
        for i in range (len(self.contacts)):
            if name == self.contacts[i].name:
                contact_exists = 'Y'
                break
        if (contact_exists == 'N'):
            self.contacts.append(PhoneContact(name, number))
            print('The contact was added')
            return True
        else:
            return False

    def export_contacts(self, file):
        with open(file,'w',newline='') as csvfile:
            writer = csv.writer(csvfile,delimiter=',')
            writer.writerow(['Name','Phone'])
            for i in range(len(self.contacts)):
                writer.writerow([self.contacts[i].name,self.contacts[i].phone])

file = ''
phone = Phone()
input_str = ''

# my program


# get input data from XML file

while True:
    try:
        file = input('\nEnter the CSV file name (contacts.csv): ')
        if file == '':
            file = 'contacts.csv'
        phone.load_contacts_from_csv(file)
        print()
        print(phone)
        print('The data from', file, 'has been loaded') 
        break
    except Exception as e:
        print(e)

input_str = input('\nWould you like to change the list? (Y/N):')

while (input_str.upper() == 'Y'):

    while (input_str.upper() == 'Y'):
        input_str = input('\nEnter: A-Add contact, R-Remove contact or E-Exit:')
        if input_str.upper() == 'A':
            name = input('\nEnter contact name:').strip()
            number = input('Enter contact phone number:').strip()
            phone.add_contact(name, number)
        elif input_str.upper() == 'R':
            name = input('\nEnter contact name to remove:').strip()
            phone.remove_contact(name)
        elif input_str.upper() == 'E':
            break
        input_str = input('\nWould you like to make other changes in contacts? (Y/N):')
        if (input_str.upper() == 'N'):
            print()
            print(phone)
            break

input_str = input('\nWould you like to export the contact list? (Y/N):')

while (input_str.upper() == 'Y'):
    file = ''
    file = input('\nEnter the file name (exported_contacts.csv): ')
    if file == '':
        file = 'exported_contacts.csv'
    phone.export_contacts(file)
    print('The contacts were exported to file', file)
    break


print('\nBye')
