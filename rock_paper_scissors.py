import random
count_computer = 0
count_user = 0
my_list = ['paper' , 'rock' , 'scissors']

while count_computer != 5 and count_user != 5:
    computer_choice = random.choice(my_list)
    user_choice = input('Choose rock (R), paper (P), or scissors (S): ').strip().lower()
    if user_choice not in ('r', 'p', 's'):
        print('Invalid choice! Please enter R, P, or S.')
        continue
    if (
            (computer_choice == 'paper' and user_choice == 'p') or
            (computer_choice == 'rock' and user_choice == 'r') or
            (computer_choice == 'scissors' and user_choice == 's')
    ):
        print("Computer chose:", computer_choice)
        print("It's a tie!")
    elif (
        (computer_choice == 'paper' and user_choice == 'r') or
        (computer_choice == 'rock' and user_choice == 's') or
        (computer_choice == 'scissors' and user_choice == 'p')
    ):
        print("Computer chose:", computer_choice)
        print('Computer scores a point!')
        count_computer += 1
    elif (
        (computer_choice == 'paper' and user_choice == 's') or
        (computer_choice == 'rock' and user_choice == 'p') or
        (computer_choice == 'scissors' and user_choice == 'r')
    ):
        print("Computer chose:", computer_choice)
        print('You score a point!')
        count_user += 1
    print(f"Score — You: {count_user} | Computer: {count_computer}")
if count_computer >= 5:
    print('computer win!')
else:
    print('user win')








