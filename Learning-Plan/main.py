i = 0
words = []
while i <= 9:
    word = input("Input the words: ")
    words.append(word)
    i = i + 1

def listToString(s):

    str1 = ""

    for ele in s:
        str1 += ele
    return str1
b =(listToString(words))

reversed = ' '.join(reversed(b))
print(reversed)