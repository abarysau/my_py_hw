# HOME WORK 5.2

print('\n----------------\nHOME WORK 5.2\n----------------\n')


print('\nПрограмма определения чисел Фибоначчи\n')

# my variables

num = ''
f = 0

# my functions

def fibo(n):

    i = 0
    fc = fp1 = fp2 = 1

    if n > 0:
        for i in range(1,n+1):
            if i > 2:
                fc = fp1 + fp2
                fp2, fp1 = fp1, fc
            print(i,fc,sep='\t')
        return fc
    else:
        return None


# my program

while num.upper() != 'E':
    
    num = input('\nEnter the end number of squence or E-Exit')

    if num.upper() == 'E':
        exit
    elif (int(num) > 0):
        f = fibo(int(num))
    else:
        print('\n***Number', num, 'is incorrect, re-enter\n')        

else:
    print('\nBye')
