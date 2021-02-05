import random
import re

# file = "data\\words.txt"

words = ['chicken']
# [line.rstrip('\n') for line in open(file)] , 'dog', 'cat', 'mouse', 'frog'
guessed_letters = []
correct = ''
guesses = 10
failed = 0
guessed = False


def target_word():
    a = random.choice(words)
    return a.upper()


t_word = target_word()
display = "_" * len(t_word)


def dictionary():
    global t_word
    dic = {}

    for i in t_word:
        dic.update({i: '_'})
    return dic


diction = dictionary()
print(diction)


def guess_word(let):
    global word, failed, guesses


    if len(let) > 1:
        word = input("Input a letter only:").upper()
    if let == '!' or guesses == 0:
        print("You made", failed, "failed attempts")
        exit()


def display_current_guess():
    global display, guessed
    for i in range(len(t_word)):
        if t_word[i] in correct:

            display = display[:i] + t_word[i] + display[i + 1:]
    for letter in display:
        print(letter, end=' ')
    print()
    if "_" not in display:
        guessed = True
    if guessed is True:
        print("You won. The correct word was", t_word)
        exit()


def hangman():
    global t_word, diction, guesses, failed, word, guessed_letters, correct

    while t_word.find(word) != -1:
        for i in guessed_letters:
            for j in diction:
                if diction[j] == word or i == word:
                    print("Already guessed that. Try again")
                    word = input("Input another letter: ").upper()
                    guess_word(word)
                    hangman()
        k = [i.start() for i in re.finditer(word, t_word)]
        print("YES", str(k))
        diction.update({word: "True"})
        correct = correct + word
        display_current_guess()
        guessed_letters.append(word)
        word = input("Input another letter: ").upper()
        guess_word(word)
        hangman()


    while t_word.find(word) == -1:
        print("NO")
        display_current_guess()
        failed = failed + 1
        guesses = guesses - 1
        guessed_letters.append(word)
        print(guesses, "more")
        word = input("Input another letter: ").upper()
        guess_word(word)
        hangman()


print("You have", guesses, "guesses")
word = input("Input a letter(To end, enter '!'):").upper()
guess_word(word)

hangman()

print(t_word)
