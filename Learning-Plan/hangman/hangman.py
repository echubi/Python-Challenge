import random
words = ["fish", "chicken", "egg", "turkey", "meat"]
a = random.choice(words)
a = a.upper()
print(a)

letter = input("Input a letter:")
letter = letter.upper()

if l in a:
    k = a.index(l)
    print("YES", +k)
else:
    print("NO")

while l not in a:
    l = input("Input a letter:")
    l = l.upper()
    if l in a:
        k = a.index(l)
        print("YES", +k)
    else:
        print("NO")