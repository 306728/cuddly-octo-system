import random, string
f = open("/cuddly-octo-system/AS/AS11/file.txt", "w")
l = []
p = []

for i in range(len(string.printable) - 5):
    l.append(string.printable[i])

for i in range(int(input("Enter password length: "))):
    p.append(random.choice(l))

f.write("".join(p))
