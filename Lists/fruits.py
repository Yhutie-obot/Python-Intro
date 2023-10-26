favorite_fruits = ['Banana', 'Paw-paw', 'Orange']
user_fruit = input('Name your favorite fruit:\n')
if user_fruit == favorite_fruits[0]:
    print('You really like' + ' ' + favorite_fruits[0])
elif user_fruit == favorite_fruits[1]:
    print('You really like' +' '+ favorite_fruits[1])
elif user_fruit == favorite_fruits[2]:
    print('You really like' +' '+ favorite_fruits[2])
else:
    print('Your favorite fruit is:' +' '+ user_fruit)