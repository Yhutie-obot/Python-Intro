alien_color = 'Yellow'
player_color = input('Guess the color:\n')
if player_color == alien_color:
    print('You\'ve just earned 5 points\n CONGRATULATIONS!!!')
elif player_color == 'Red':
    print('You have earned 10points but try again')
elif player_color == 'Green':
    print('You just earned 15 points, wow')
else:
    print('Try again next time')