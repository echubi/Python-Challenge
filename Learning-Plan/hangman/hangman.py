import random

def target_word():
    words = ["fish", "chicken", "egg", "turkey", "meat"]
    a = random.choice(words)
    a = a.upper()
    return a

def dictionary():
    dic = {}
    for i in target_word():
        dic.update({i: 'False'})
    print(dic)
    return dic

#dictionary()

l = input("Input a letter(To end, enter '!'):")

def logic(l):
    guess = 0
    while len(l) > 1:
        l = input("Input a letter only:")
    if l == '!':
        exit()
    l = l.upper()

    if l in target_word():
        k = target_word.index(l)
        print("YES", +k)
        dictionary().update({l: "true"})
        #print(dic)
    else:
        print("NO")

    while l not in target_word():
        guess = guess + 1
        l = input("Input a letter:")
        l = l.upper()
        if l in target_word():
            k = target_word().index(l)
            print("YES", +k)
        else:
            print("NO")
            
