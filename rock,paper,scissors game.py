import random

options=("rock","paper","scissors")
computer=random.choice(options)
total_rounds=int(input("Enter the number of rounds to play(best of N): "))
computer_win=0
player_win=0
tie=0
no_rounds=0

print(f"🎮ROCK PAPER SCISSORS BEST OF {total_rounds}🎮")
while no_rounds < total_rounds:
    print(f"\nROUND {no_rounds+1} OUT OF {total_rounds}")
    computer=random.choice(options)
    player=input("Enter the choice(rock,paper,scissors or 'q' for quit): ").lower()
    
    if player == 'q':
        print("EXITING...")
        print("THANKING YOU FOR PLAYING")
        break
    
    
    if player in options:
        print(f"{'PLAYER':10}:{player}")
        print(f"{'COMPUTER':10}:{computer}")
        if player == computer:
            print("🤝 It's tie")
            tie+=1
        elif player == "rock":
            if computer == "paper":
                print("🧻 Paper cover rock! 'YOU LOSE..'")
                computer_win+=1
            else:
                print("🪨 Rock smash scissors! 'YOU WIN!'")
                player_win+=1
        elif player == "paper":
            if computer == "rock":
                print("🧻 Paper cover rock! 'YOU WIN!'")
                player_win+=1
            else:
                print("✂ Scissors cut paper! 'YOU LOSE..'")
                computer_win+=1
        elif player == "scissors":
            if computer == "paper":
                print("✂ Scissors cut paper! 'YOU WIN!'")
                player_win+=1
            else:
                print("🪨 Rock smash scissors! 'YOU LOSE..'")
                computer_win+=1
        no_rounds += 1
    else:
        print("Invalid choice.Please enter the rock,paper,scissors or 'q'.")
        

print("\nGAME RECORD".center(50))
print('-'*35)
print(f"{'PLAYER WINS':20}: {player_win}")
print(f"{'COMPUTER WINS':20}: {computer_win}")
print(f"{'TIES':20}: {tie}")
print(f"{'TOTAL ROUNDS PLAYED':20}: {no_rounds}")
print('-'*35)

if  player_win > computer_win:
    print("\n***🧑YOUR ARE THE FINAL WINNER🎉***")
elif player_win < computer_win:
    print("\n***🤖COMPUTER WINS THE GAME.BETTER LUCK NEXT TIME🎉***")
else:
    print("\n***🤝IT'S A TIE***")        
        


    
    
