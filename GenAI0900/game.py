import random

emoji = {'r': '🪨', 's': '✂️', 'p': '📃'}
choices = ('r', 'p', 's')

while True:
    user_choice = input(
        "please enter the rock, paper, scissors? (r/s/p): ").lower()

    if user_choice not in choices:
        print('invalid choice!')
        continue

    computer_choice = random.choice(choices)

    print(f'you choose {emoji[user_choice]}')
    print(f'computer choose {emoji[computer_choice]}')

    if user_choice == computer_choice:
        print('IT IS TIE')
    elif ((user_choice == 'r' and computer_choice == 's') or
          (user_choice == 'p' and computer_choice == 'r') or
          (user_choice == 's' and computer_choice == 'p')):
        print('you win')
    else:
        print('YOU LOSE')

    wanna_continue = input('if you want to continue (y/n)? : ').lower()
    if wanna_continue == 'n':
        break
