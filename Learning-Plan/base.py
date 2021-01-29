base = int(input("Input the desired base:"))
while base < 2 or base > 16 or base == 10:
    base = int(input("Input a base between 2 and 16:"))

num = int(input("Input the number:"))
while num < 1:
    num = int(input("Input the number:"))


def convert(x, y):
    if x == 0:
        return
    z = x % y
    x //= y
    if z < 0:
        x += 1

    convert(x, y)

    if z < 0:
        print(z + (y * -1), end = " ")
    else:
        print(z, end = " ")


def conv(x, y):
    print("Number", x, "in base", y, "is:", end = " ")
    
    if x != 0:
        convert(x, y)
    else:
        print("0", end = " ")


conv(num, base)
