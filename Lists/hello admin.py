users = ['admin', 'Itoro', 'Joshua', 'Afia', 'Uduak']
user_name = input('Enter your username:\n')
if user_name == users[0]:
    print('Hello' +' '+ users[0]+' '+ 'Welcome!\n what changes would you like to effect today:')
elif user_name == users[:4]:
    print('Hi' + ' ' + user_name + ' ' + 'Welcome')
else:
    print('Unrecognised')
