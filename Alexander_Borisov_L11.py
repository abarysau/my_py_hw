# HOME WORK 11

print('\n----------------\nHOME WORK 11\n----------------\n')

print('ToDo sample program')

# imported mjdules

import sqlite3 as sql

# my objects & variables

class ToDoException(Exception):
    ''' Class for ToDo exceptions '''

    def __init__(self, message=''):
        super().__init__(self)
        self.my_message = message
    def __str__(self):
        return str((self.my_message))

class BadLine(ToDoException):
    def __init__(self, bad_element, message='Bad input data'):
        super().__init__(self)
        self.bad_element = bad_element
        self.my_message = message
    def __str__(self):
        return str((self.bad_element, self.my_message))

    
class ToDo:
    ''' Class for ToDo application '''
    
    def __init__(self, file_name):
        self.conn = sql.connect(file_name)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        print('\nCreate database table, if not exists')
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks_list (
                 task_id INTEGER PRIMARY KEY
                ,task_name TEXT NOT NULL
                ,task_prio INTEGER NOT NULL
                );''')
                
    def show_tasks(self):
        print('\n ToDo list contains the following tasks:')
        print('-'.rjust(12,'-'), '-'.ljust(30,'-'), '-'.rjust(12,'-'))
        print('TASK_ID'.rjust(12), 'TASK_NAME'.ljust(30), 'TASK_PRIO'.rjust(12))
        print('-'.rjust(12,'-'), '-'.ljust(30,'-'), '-'.rjust(12,'-'))
        for row in self.c.execute('''SELECT task_id, task_name, task_prio
                                    FROM tasks_list
                                    ;'''):
            print(str(row[0]).rjust(12), row[1].ljust(20), str(row[2]).rjust(12))
        
            
    def add_task(self):
        self.name = input('Enter task name:')
        self.prio = input('Enter task priority:')
        if (len(self.name.strip()) == 0):
            raise BadLine(self.name,'***Incorrect task name')
        elif not self.prio.isdecimal():
            raise BadLine(self.prio,'***Incorrect task prio')
        self.c.execute('''INSERT INTO tasks_list (task_name, task_prio)
                        VALUES (?, ?);''', (self.name, self.prio))
        self.conn.commit()

    def delete_task(self):
        self.id = input('Enter task id to delete:')
        self.c.execute('''DELETE FROM tasks_list WHERE task_id = ?
                        ;''',(self.id))
        if ((self.c.rowcount) == 0):
            raise BadLine(self.id,'***Requested task id was not found')
        self.conn.commit()

    def update_prio(self):
        self.id = input('Enter task id to update:')
        self.prio = input('Enter new task priority:')
        if not self.prio.isdecimal():
            raise BadLine(self.prio,'***Incorrect task prio')
        self.c.execute('''UPDATE tasks_list SET task_prio = ? WHERE task_id = ?
                        ;''',(self.prio, self.id))
        if ((self.c.rowcount) == 0):
            raise BadLine(self.id,'***Requested task id was not found')
        self.conn.commit()

    def close_conn(self):
        self.conn.close()
        print('\nConnection is closed')
        
file_name = ''

# my functions

def print_app_menu():

    while True:
        print('''
         -----------------
        | S - Show        |
        | A - Add task    |
        | D - Delete task |
        | U - Update prio |
        | E - Exit        |                 
         -----------------''')      
        oper = input('\nEnter operation number:\n') 
        if (oper.upper() == 'E'):
            return False
        else:
            if (oper.upper() == 'S'):
                app.show_tasks()
            elif (oper.upper() == 'A'):
                app.add_task()
            elif (oper.upper() == 'D'):
                app.delete_task()
            elif (oper.upper() == 'U'):
                app.update_prio()    
            return True


# my program


while True:
    try:
        file_name = input('\nEnter Database file name: ')
        app = ToDo(file_name)
        while True:
            try:
                if not print_app_menu():
                    break
            except Exception as tde:
                print(tde)
        app.close_conn()        
        break
    except:
        print('There is something wrong')


print('\nBye')
