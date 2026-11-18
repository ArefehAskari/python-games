import random
count_computer = 0
count_user = 0
my_list = ['paper' , 'rock' , 'scissors']

while count_computer != 5 and count_user != 5:
    computer_choice = random.choice(my_list)
    user_choice = input('plese enter your choice : R , P , S ')
    if (
            (computer_choice == 'paper' and user_choice == 'P') or
            (computer_choice == 'rock' and user_choice == 'R') or
            (computer_choice == 'scissors' and user_choice == 'S')
    ):
        print('same ! try again')
    elif (
        (computer_choice == 'paper' and user_choice == 'R') or
        (computer_choice == 'rock' and user_choice == 'S') or
        (computer_choice == 'scissors' and user_choice == 'P')
    ):

        print('+1 score for computer')
        count_computer += 1

    elif (
        (computer_choice == 'paper' and user_choice == 'S') or
        (computer_choice == 'rock' and user_choice == 'P') or
        (computer_choice == 'scissors' and user_choice == 'R')
    ):
        print('+1 score for user')
        count_user += 1
if count_computer >=5:
    print('computer win!')
else:
    print('user win')








