first = input("Input your name:")
second = input("Input your partner's name:")

names = first + "loves" + second
a = []
sum = 0

for i in names:
    x = names.count(i)
    a.append(x)

for j in range(0, len(a)):
    sum = sum +  a[j]

print("The love percentage is", sum, "%")
