# HOME WORK 7.1

print('\n----------------\nHOME WORK 7.1\n----------------\n')


print('\nSystem Info Program\n')

# my modules

import platform

# my variables

req = ''

# my program

while req.upper() != 'EXIT':
    req = input('\nEnter your Request (SYSTEM, MACHINE, PYTHON) or EXIT:')

    if req.upper() == 'SYSTEM':
        print('Operation system = ', platform.system())
        print('Release = ', platform.release())

    elif req.upper() == 'MACHINE':
        print('Machine type = ', platform.machine())
        print('Processor = ', platform.processor())
        print('Node = ', platform.node())

    elif req.upper() == 'PYTHON':
        print('Python impementation = ',platform.python_implementation())
        print('Version = ',platform.python_version())
        print('Compiler = ',platform.python_compiler())

    elif req.upper() == 'EXIT':
        pass

    else:
        print('\nUnknown command, re-enter') 

else:
    print('\nBye')



           
