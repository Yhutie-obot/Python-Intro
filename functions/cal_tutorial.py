def add(a, b):
    answer = a + b
    print(str(a) +'+'+ str(b) +'='+ str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) +'-'+ str(b) +'='+ str(answer))

def mul(a, b):
    answer = a * b
    print(str(a) +'*'+ str(b) +'='+ str(answer))

def div(a, b):
    answer = a / b
    print(str(a) +'/'+ str(b) +'='+ str(answer))
while True:
    print('A. Addition')
    print('B. Subtraction')
    print('C. Multiplication')
    print('D. Division')
    print('E. Exit')
    break
choice = input('Enter your choice:\n')

if choice == 'A' or choice == 'a':
    print('Addition')
    a = int(input('Enter first number:\n'))
    b = int(input('Enter second number:\n'))
    add(a, b)
elif choice =='B' or choice == 'b':
    print('Subtraction')
    a = int(input('Enter first number:\n'))
    b = int(input('Enter second number:\n'))
    sub(a, b)

elif choice == 'C' or choice == 'c':
    print('Multiplication')
    a = int(input('Enter first number:\n'))
    b = int(input('Enter second number:\n'))
    mul(a, b)

elif choice == 'D' or choice == 'd':
    print('Division')
    a = int(input('Enter first number:\n'))
    b = int(input('Enter second number:\n'))
    div(a, b)
elif choice == 'E' or choice == 'e':
    print('Program Ended')
    quit()




