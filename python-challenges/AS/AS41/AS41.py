import random
n = []

for _ in range(7):
    n.append(str(random.randint(0, 1)))

p = random.choice(["ODD", "EVEN"])

a = int(input(f"{p} parity in use. The number is: _{''.join(n)}. What is the parity bit?: "))

match p:
    case "ODD":
        if a == 1 and n.count("1") % 2 == 0:
            print("Your answer is correct.")
        elif a == 1 and n.count("1") % 2 == 1:
            print("Your answer is incorrect. The parity bit is 0.")
        elif a == 0 and n.count("1") % 2 == 0:
            print("Your answer is incorrect. The parity bit is 1.")
        else:
            print("Your answer is correct.")
    case "EVEN":
        if a == 0 and n.count("1") % 2 == 0:
            print("Your answer is correct.")
        elif a == 0 and n.count("1") % 2 == 1:
            print("Your answer is incorrect. The parity bit is 1.")
        elif a == 1 and n.count("1") % 2 == 0:
            print("Your answer is incorrect. The parity bit is 0.")
        else:
            print("Your answer is correct.")
