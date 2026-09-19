import numpy as np
choices = ["Rock", "Paper", "Scissor"]
def game():
    a = np.random.choice(choices)
    b = input("Enter one between Rock Paper Scissor: ").strip().capitalize()
    
    if b not in choices:
        print("Invalid choice! Please try again.")
        return
        
    print(f"Computer Choice {a} and Your Choice {b}")
    
    if a == b:
        print("It's a Tie")
    elif (a == "Paper" and b == "Scissor") or \
         (a == "Rock" and b == "Paper") or \
         (a == 'Scissor' and b == 'Rock'):
        print("You Won")
    else: 
        print("Computer Won")
    d = int(input("Do you want to play again \n1.Play Game \n2.Exit \n"))
    if d == 1:
        game()
    elif d == 2:
        print("Thanks for playing")

print("Hi Welcome to Rock Paper Scissor Game")
game()
