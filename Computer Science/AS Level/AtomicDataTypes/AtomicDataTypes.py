import random, string
from datetime import datetime, timedelta

lives = random.randint(3, 6)
n = random.randint(10, 20)
c = 0

print(f"You have {lives} lives.")
print(f"There are a total of {n} questions.")

while lives != 0 and n != 0:
    data = [random.randint(0, 100), float(random.randint(0, 100)/random.randint(1, 100)), ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1, 10))), datetime.now() - timedelta(days=random.randint(365*2, 365*4), hours=random.randint(0, 23), minutes=random.randint(0, 59)), True, False]
    q = random.choice(data)
    a = input(f"What is the data type of {q}? ")
    if type(q) is str and len(q) == 1 and a == "CHAR" or type(q) is str and len(q) > 1 and a == "STRING" or type(q) is int and a == "INTEGER" or type(q) is float and a == "REAL" or type(q) is datetime and a == "DATE" or type(q) is bool and a == "BOOLEAN":
        print("Correct!")
        c += 1
    else:
        print("Your guess is incorrect.")
        lives -= 1
    n -= 1
    print(f"You have {lives} lives left.")
    print(f"{n} questions remain.")

print(f"You answered {c} questions correctly.")

if n == 0 and lives != 0:
    print("Congratulations! You have mastered atomic data types.")
else:
    print("Better luck next time.")
