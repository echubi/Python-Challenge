base = int(input("Input the desired base:"))
while base < 2 or base > 16 or base == 10:
    base = int(input("Input a base between 2 and 16:"))

num = int(input("Input the number:"))
while num < 1:
    num = int(input("Input the number:"))

def convert(x,y):
    if (x == 0):
        return;
    z = x % y;
    x //= y;
    if(z < 0):
        x += 1;

    convert(x,y)

    if (z < 0):
        print(z + (y * -1), end = " ");
    else:
        print(z, end = " ")

def conver(x,y):
    print(" Number", x,"in base",y, "is:", end = " ");
    
    if (x != 0):
        convert(x,y)
    else:
        print("0", end = " ")


conver(num,base)
"""
def base(nu,n):
    nu_rep = { 10: 'A',
                11: 'B',
                12: 'C',
                13: 'D',
                14: 'E',
                15: 'F'}
    new_nu_string = ''
    current = int(nu)
    while current != 0:
        remainder = current % int(n)
        if 16 > remainder > 9:
            remainder_string = nu_rep[remainder]
        elif remainder >= 16:
            remainder_string = '("+str(remainder)+")'
        else:
            remainder_string = str(remainder)
        new_nu_string = remainder_string + new_nu_string
        current = current // int(n)
    return new_nu_string

base(num,base)"""
