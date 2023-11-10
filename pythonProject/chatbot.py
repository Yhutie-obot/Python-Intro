import paymentmethod
import Account_Details

food_list = ['Editan', 'Afang', 'Ekwong', 'White-soup', 'Atama']
print('Welcome to YHUTIEPLUS KITCHEN')
client = input('May I get your name please: ')
print('Hi' +' ' + client + ' ' 'I am your waitress and I am pleased to have you at YHUTIEPLUS KITCHEN')
print('Here is our menu:')
for food_list in food_list:
    print(food_list.upper())
print(client + ' ' + ' What is your meal choice:')
meal = input('Type here: ')
if meal == food_list[0]:
    print(pm)
    print('Choose your payment method: ')
    if pm == pm[0]:
        print(food_list[0] + ' ' + 'is served')
    elif pm == pm[1]:
        print(pm[1] + ' ' + 'is on the way')
    elif pm == pm[2]:
        print(ad)
        
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
