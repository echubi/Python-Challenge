from . utils import *
import re
import string


guessed_letters = []
correct = ''
guesses = 10
failed = 0
guessed = False


class Hangman:
    def __init__(self, target):
        self.target = target

    def dictionary(self):
        dic = {}

        for i in self.target:
            dic.update({i: 'False'})
        return dic

    def guess_word(self):
        global word, failed, guesses
        alphabet_upper = string.ascii_uppercase
        alphabet_uppers = list(alphabet_upper)
        if len(word) > 1 or word not in alphabet_uppers:
            word = input("Your input must be a single character alphabet or '!' to exit: ").upper()
            self.guess_word()
        if word == '!' or guesses == 0:
            print("You made", failed, "failed attempts")
            print("The correct word is", self.target)
            exit()

    def display_current_guess(self):
        global display, guessed
        for i in range(len(self.target)):
            if self.target[i] in correct:
                display = display[:i] + self.target[i] + display[i + 1:]
        for letter in display:
            print(letter, end=' ')
        print()
        if "_" not in display:
            guessed = True
        if guessed is True:
            print("You won. The correct word was", self.target)
            exit()

    def run(self):
        global guesses, failed, word, guessed_letters, correct

        while self.target.find(word) != -1:
            for i in guessed_letters:
                for j in self.dictionary():
                    if self.dictionary()[j] == word or i == word:
                        print("Already guessed that. Try again")
                        word = input("Input another letter: ").upper()
                        self.guess_word()
                        self.run()
            k = [i.start() for i in re.finditer(word, self.target)]
            print("YES", str(k))
            self.dictionary().update({word: "True"})
            correct = correct + word
            self.display_current_guess()
            guessed_letters.append(word)
            word = input("Input another letter: ").upper()
            self.guess_word()
            self.run()

        while self.target.find(word) == -1:
            print("NO")
            self.display_current_guess()
            failed = failed + 1
            guesses = guesses - 1
            guessed_letters.append(word)
            print(guesses, "more")
            word = input("Input another letter: ").upper()
            self.guess_word()
            self.run()


t_word = target_word()
display = "_" * len(t_word)
print(display)
print("You have", guesses, "guesses")
word = input("Input a letter(To end, enter '!'):").upper()
