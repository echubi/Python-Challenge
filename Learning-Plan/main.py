import random
random_word_list = \
['hiroshima ', 'me ', 'you ', 'my-ex ', 'dog-fight ', 'charley ', 'abortion ', 'aid ', 'center ', 'claim ', 'common ', 'crime ', 'divorce ', 'essential ', 'fear ', 'height ', 'helpful ', 'insight ', 'label ']

i = 0
random_wordr = []
while i <= 10:
    random_words = random_word_list[random.randint(0, 20)]
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