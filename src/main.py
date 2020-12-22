import random

choices = ['rock','paper','scissors']

ai_score = 0
user_score = 0

def spelling_error_handling(correct_word_choices,prompt):
    user_word_choice = input(prompt).lower()
    if user_word_choice in correct_word_choices:
        return user_word_choice
    is_word_correct = False
    while is_word_correct is False:
        if user_word_choice in correct_word_choices:
            is_word_correct = True
        else:
            print('Check spelling :)')
            user_word_choice = input(prompt).lower()
    return user_word_choice

def ai_selection():
    return random.choice(choices)

def user_selection():
    user_choice = spelling_error_handling(['rock','paper','scissors'],'Which will you go with? Rock Paper or Scissors? ')
    return user_choice

def who_won(ai,user):
    if ai == user:
         return 'None'

    if ai == 'rock' and user == 'scissors':
        return 'ai' 
    elif ai == 'rock' and user == 'paper':
        return 'user'

    if ai =='paper' and user == 'rock':
        return 'ai'
    elif ai == 'paper' and user == 'scissors':
        return 'user'

    if ai == 'scissors' and user == 'paper':
        return 'ai'
    elif ai == 'scissors' and user == 'rock':
        return 'user'



def main():
    ai_score = 0
    user_score = 0

    play = True
    while play:
        ai_choice = ai_selection()
        user_choice = user_selection()
        winner = who_won(ai_choice, user_choice)
        if winner == 'ai':
            print('Ooo Ai chose', ai_choice, ':(')
            ai_score += 1
        else:
            print('Congrats!! :)')
            user_score += 1
        print("User Score: ", user_score," | Ai Score: ", ai_score)
        play = spelling_error_handling(['no','n','yes','y'],'Want to play again?(Y/N) ')
        if play == 'n' or play == 'no':
            play = False
            return
        else:
            play = True
    print("User Score: ", user_score," | Ai Score: ", ai_score)

main()
