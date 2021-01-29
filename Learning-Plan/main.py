i = 0
words = []
while i <= 9:
    word = input("Input the words: ")
    words.append(word)
    i = i + 1


def listtostring(s):


    str1 = ""

    for ele in s:
        str1 += ele
    return str1


b = (listtostring(words))


reverse = ' '.join(reversed(b))
print(reverse)
