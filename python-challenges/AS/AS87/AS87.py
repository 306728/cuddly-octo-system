word1 = input()
word2 = input()
l = []

if len(word1) > len(word2):
    for i in range(len(word2)):
        l.append(word1[i] + word2[i])
    l.append(word1[len(word2):])
elif len(word2) > len(word1):
    for i in range(len(word1)):
        l.append(word1[i] + word2[i])
    l.append(word2[len(word1):])
else:
    for i in range(len(word1)):
        l.append(word1[i] + word2[i])

print("".join(l))
