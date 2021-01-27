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
    failed = len(diction) + 5

    print(diction)
    while len(let) > 1:
        let = input("Input a letter only:").upper()
    if let == '!' or failed == 0:
        print(diction)
        print("You made", guess, "failed attempts")
        exit()

    if let in diction:
        k = list(diction).index(let)
        print("YES", +k)
        diction.update({let: "True"})
    else:
        print("NO")
        guess = guess + 1
        failed = failed - 1

    while let not in diction:

        let = input("Input a letter:").upper()
        if let == '!' or failed == 0:
            print(diction)
            print("You made", guess, "failed attempts")
            exit()
        if let in diction:
            k = list(diction).index(let)
            print("YES", +k)
            diction.update({let: "True"})
        else:
            print("NO")
        guess = guess + 1
        failed = failed - 1



logic(word)
