monsters = {}
with open("monsters.txt", "r") as f:
    for line in f:
        l = line.strip().split(",")
        monsters[l[0]] = l[1]

print(monsters[input("Enter monster name: ")])
