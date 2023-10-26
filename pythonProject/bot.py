user_name = input('what is ur name?' + ' ')
print('hi' + ' ' + user_name + ' ' + 'How may I be of help today?')
meal = ['Afang', 'Okra', 'Bole']
Afang = ('Afang')
Okra = ('Okra')
Bole = ('Bole')
print('Please kindly choose your meal' + ' ' + user_name )
print(Afang)
print(Okra)
print(Bole)
choice = input('Kindly choose a meal option:' + ' ')
if choice == Afang:
    print(user_name + ' Your request for Afang is being processed: $2000 USD')
if choice == Okra:
        print(user_name + ' Your request for Okra is being processed: $1500 USD')
if choice == Bole:
    print(user_name + ' Your request for Bole is being processed: $200 USD')
if choice != meal:
    print('Sorry' + ' ' + user_name + ' ' + 'Your choice of meal is not available')

print(food_list[0])
print(food_list[1])
print(food_list[2])
print(food_list[3])
print(food_list[4])