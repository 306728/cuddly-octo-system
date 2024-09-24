import random, string
from datetime import datetime, timedelta

data = ["Python", "Pyth0n", random.randint(0, 100), float(random.randint(0, 100)/random.randint(1, 100)), ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(2, 10))), random.choice(string.ascii_letters), datetime.now() - timedelta(days=random.randint(365*2, 365*4), hours=random.randint(0, 23), minutes=random.randint(0, 59))]
lives = 3

for i in range(10):
    q = random.choice(data)
    print(type(q))
    a = input(f"What is the data type of {q}? ")