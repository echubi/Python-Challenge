import random

words = ["fish", "chicken", "egg", "turkey", "meat"]


def target_word():
    a = random.choice(words)
    return a.upper()


def dictionary():
    dic = {}
    t_word = target_word()
    for i in t_word:
        dic.update({i: 'False'})

    return dic


word = input("Input a letter(To end, enter '!'):").upper()


def logic(let):


    guess = 0
    diction = dictionary()

    print(diction)
    while len(let) > 1:
        let = input("Input a letter only:").upper()
    if let == '!':
        print(dictionary())
        exit()

    if let in diction:
        k = list(diction).index(let)
        print("YES", +k)
        dictionary().update({let: "true"})
    else:
        print("NO")

    while let not in diction:

        let = input("Input a letter:").upper()
        if let in target_word():
            k = list(diction).index(let)
            print("YES", +k)
        else:
            print("NO")
        guess = guess + 1

logic(word)