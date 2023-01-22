import random
# Rock, Paper and Scissors.
def gameWin(comp, you):
    # If the values are  same.
    if comp == you:
        return None
# Checking all possibilities when a computer choose Scissor
    elif comp == 's':
        if you =='p':
            return False
        elif you =='r':
            return True
# Checking all possibilities when a computer choose Paper
    elif comp == 'p':
        if you =='r':
             return False
        elif you == 's':
            return True
# Checking all possibilities when a computer choose Rock       
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
  
print("Comp turn: Rock(r), Paper(p), Scissor(s) ?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your turn: Rock(r), Paper(p), Scissor(s) ?")
a = gameWin(comp, you)

print(f"Computer choose {comp}")
print(f"You choose {you}")
if a == None:
    print("Oops!, The game is tie :|")
elif a:
    print("You win the game :)")
else:
    print("You lose the game :(")

