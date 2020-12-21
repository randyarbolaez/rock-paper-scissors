import random

choices = ['rock','paper','scissors']

ai_score = 0
user_score = 0

def ai_selection():
    return random.choice(choices)

def user_selection():
    user_choice = input('Which will you go with? Rock Paper or Scissors? ').lower()
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
        play = input('Want to play again?(Y/N)').lower()
        if play == 'n':
            play = False
            return
        else:
            play = True
    print("User Score: ", user_score," | Ai Score: ", ai_score)

main()
