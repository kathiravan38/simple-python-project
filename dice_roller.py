import random

#print("\u250C \u2500 \u2510 \u2502 \u2514 \u2518 \u25CF \u0020") output:┌ ─ ┐└ ┘│●

dices={1:("┌───────┐",
          "│       │",
          "│   ●   │",
          "│       │",
          "└───────┘"),
       2:("┌───────┐",
          "│ ●     │",
          "│       │",
          "│     ● │",
          "└───────┘"),
       3:("┌───────┐",
          "│ ●     │",
          "│   ●   │",
          "│     ● │",
          "└───────┘"),
       4:("┌───────┐",
          "│ ●   ● │",
          "│       │",
          "│ ●   ● │",
          "└───────┘"),
       5:("┌───────┐",
          "│ ●   ● │",
          "│   ●   │",
          "│ ●   ● │",
          "└───────┘"),
       6:("┌───────┐",
          "│ ●   ● │",
          "│ ●   ● │",
          "│ ●   ● │",
          "└───────┘"),}
    
dice=[]
total=0
num_of_dice=int(input("Enter how many dice?"))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

print("\n🎲ROLLING...")
for i in range(0,num_of_dice,5):
    for line in range(5):
        for die in dice[i:i+5]:
            print(dices.get(die)[line],end=" ")
        print()
        

for die in dice:
    total+=die
print(f"\nTOTAL: {total}")
