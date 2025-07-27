import random
user = input("Choose rock, paper or scissors: ")
comp = random.choice(["rock", "paper", "scissors"])
print(f"Computer chose: {comp}")
if user == comp:
    print("Draw!")
elif (user == 'rock' and comp == 'scissors') or (user == 'paper' and comp == 'rock') or (user == 'scissors' and comp == 'paper'):
    print("You win!")
else:
    print("You lose!")