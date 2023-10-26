food_list = ['Editan', 'Afang', 'Ekwong', 'White-soup', 'Atama']
payment_method = ['Cash', 'PoS', 'Transfer']
Account_Details = ['Account Number: 0043214509', 'Account name: Yhutieplus kitchen', 'Bank name: Opay']

print('Welcome to YHUTIEPLUS KITCHEN')
client = input('May I get your name please: ')
print('Hi' +' ' + client + ' ' 'I am your waitress and I am pleased to have you at YHUTIEPLUS KITCHEN')
print('Here is our menu:')
for food_list in food_list:
    print(food_list.upper())
print(client + ' ' + ' What is your meal choice:')
meal = input('Type here: ')
if meal == food_list[0]:
    print(payment_method)
    print('Choose your payment method: ')
    if payment_method == payment_method[0]:
        print(food_list[0] + ' ' + 'is served')
    elif payment_method == payment_method[1]:
        print(payment_method[1] + ' ' + 'is on the way')
    elif payment_method == payment_method[2]:
        print(Account_Details)
        
else:
    if meal == food_list[1]:
        print(food_list[1] + ' ' + 'is served')
    elif meal == food_list[2]:
        print(food_list[2] + ' ' + 'is served')
    elif meal == food_list[3]:
        print(food_list[3] + ' ' + 'is served')
    elif meal == food_list[4]:
        print(food_list[4] + ' ' + 'is served')
if meal != food_list:
    print(meal + ' ' + 'is not on our list please')
else:
    print('Enjoy your delicious' + ' ' + meal)
