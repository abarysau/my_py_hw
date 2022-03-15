# HOME WORK 5.1

print('\n----------------\nHOME WORK 5.1\n----------------\n')


print('\nПрограмма вычисления факториала (используется функция без рекурсии)\n')

# my variables

num = ''
f = 0

# my functions

def factorial(n):

    i = 0
    f = 1

    if n >= 0:
        for i in range(n+1):
            if i > 1:
                f = f * i
            print(i,f)
        return f
    else:
        return None


# my program

while num.upper() != 'E':
    
    num = input('\nEnter Number or E-Exit')

    if num.upper() == 'E':
        exit
    elif (int(num) >= 0):
        f = factorial(int(num))
        print('\nFactorial of', int(num), 'is', f)
    else:
        print('\n***Number', num, 'is incorrect, re-enter\n')        

else:
    print('\nBye')
