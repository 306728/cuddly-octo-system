import random

m = ["rock", "paper", "scissors"]
a = "yes"
s_p = 0
s_c = 0

while a == "yes":
    p = input("Rock, paper or scissors: ").lower()
    c = random.choice(m)
    print(f"You chose: {p}\nComputer chose: {c}")
    if p == c:
        print("Draw!")
    elif p == "rock":
        if c == "paper":
            print("Computer wins!")
            s_c += 1
        elif c == "scissors":
            print("You win!")
            s_p += 1
    elif p == "paper":
        if c == "rock":
            print("You win!")
            s_p += 1
        elif c == "scissors":
            print("Computer wins!")
            s_c += 1
    elif p == "scissors":
        if c == "rock":
            print("Computer wins!")
            s_c += 1
        elif c == "paper":
            print("You win!")
            s_p += 1
    print(f"Score: Player {s_p}-{s_c} Computer")
    a = input("Do you wish to continue? (yes/no): ")
print(f"Final score: Player {s_p}-{s_c} Computer")
