v = ["a", "e", "i", "o", "u"]

def make_it_laugh(s):
    l = list(s)
    for i in range(len(l)):
        if l[i] in v:
            l[i] = "haha"
    return "".join(l)

print(make_it_laugh(input()))
