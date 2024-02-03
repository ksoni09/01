

a = int(input('Enter the value 1: '))
b = int(input('Ener the Value 2: '))
 
opertaion = input('choose operation (+, -, *, /):')

if opertaion == "+":
    print('the result is ' + str(a+b))
elif opertaion == '-':
    print('the result is ' + str(a-b))
elif opertaion == '*':
    print('the result is ' + str(a*b))
elif opertaion == '/' and b != 0:
    print('the result is ' + str(a/b))
else: 
    print('error')
    
