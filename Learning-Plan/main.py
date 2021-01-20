i = 0
random_wordr = []
while i <= 9:
    random_words = input("Input the words: ")
    random_wordr.append(random_words)
    i = i + 1

print(random_wordr)

def listToString(s):

    str1 = ""

    for ele in s:
        str1 += ele
    return str1
b =(listToString(random_wordr))

reversed = ''.join(reversed(b))
print(reversed)