import random
c = 7
l = open("/workspaces/cuddly-octo-system/AS/AS05/file.txt").read().splitlines()
w = random.choice(l)
a = []

for i in range(len(w)):
    a.append("_")

while c != 0:
    print("".join(a))
    g = input("Guess a letter or the entire word: ")
    if g == w:
        print(f"You win! The word was: {w}.")
        break
    elif g in w:
        for i in range(len(w)):
            if g == w[i]:
                a[i] = g
    else:
        c -= 1
        print(f"Your guess was incorrect. {c} attempts remaining.")
else:
    print(f"You lost! The word was: {w}.")
