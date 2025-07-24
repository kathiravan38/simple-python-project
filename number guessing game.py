#number guessing game
import random

#input
low=1
high=100
computer_guess=random.randint(low,high)
guesses=0

#game main function
print("🎮NUMBER GUESSING GAME🎮")
print("select the number between 1 to 100")
while True:
    player_guess=input("select the guess(q for quit): ")
    if player_guess.lower() == 'q':
        print("GAME EXITED...")
        break
    
    if player_guess.isdigit():
        player_guess=int(player_guess)
        if player_guess <= high and player_guess >= low:
            guesses+=1
            if player_guess == computer_guess:
                print("**✅CORRECT!✅**")
                break
            elif player_guess > computer_guess:
                print("--⬆️TOO HIGH⬆️,TRY AGAIN--")
            else:
                print("--⬇️TOO LOW⬇,TRY AGAIN--")
        else:
            print(f"-please enter a number between {low} to {high}-")
       
    else:
        print(f"invalid guess!\nplease enter the number between {low} to {high}")
    
#print guesses   
if guesses>0:
    print(f"**YOUR GUESSES IT IN {guesses} ATTEMPTS**")
        



