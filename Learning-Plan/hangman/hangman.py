import random
words = ["fish", "chicken", "egg", "turkey", "meat"]
a = random.choice(words)
a = a.upper()
print(a)
dic = {}
guess = 0
for i in a:
    dic.update({i: 'false'})

l = input("Input a letter(To end, enter '!'):")
while len(l) > 1:
    l = input("Input a letter only:")
if l == '!':
    exit()
l = l.upper()

if l in a:
    k = a.index(l)
    print("YES", +k)
    dic.update({l: "true"})
    print(dic)
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

