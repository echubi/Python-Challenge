from rich.console import Console
from rich.style import Style
from .utils import *
import re
from.database import *

console = Console(color_system="windows")

guessed_letters = []
correct = ''
guesses = 10
failed = 0
guessed = False

create_db()


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

        if len(word) > 1:
            word = input("Input a letter only:").upper()
        if word == '!' or guesses == 1:
            print("You made", failed, "failed attempts")
            console.print("The correct word is", self.target, style="#FFC0CB")
            c.close()
            conn.close()
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
            console.print("You won. The correct word was", self.target, style="blue")

            c.close()
            conn.close()
            exit()

    def run(self):
        global guesses, failed, word, guessed_letters, correct

        while self.target.find(word) != -1:
            for i in guessed_letters:
                for j in self.dictionary():
                    if self.dictionary()[j] == word or i == word:
                        console.print("Already guessed that. Try again", style="#FFA500")

                        word = input("Input another letter: ").upper()
                        self.guess_word()
                        self.run()
            k = [i.start() for i in re.finditer(word, self.target)]
            console.print("YES", str(k), style="green")
            self.dictionary().update({word: "True"})
            correct = correct + word
            self.display_current_guess()
            data_entry(word)

            guessed_letters.append(word)
            word = input("Input another letter: ").upper()
            self.guess_word()
            self.run()

        while self.target.find(word) == -1:
            for i in guessed_letters:
                for j in self.dictionary():
                    if self.dictionary()[j] == word or i == word:
                        console.print("Already guessed that. Try again", style="#FFA500")
                        word = input("Input another letter: ").upper()
                        self.guess_word()
                        self.run()
            console.print("NO", style="red")
            self.display_current_guess()
            failed = failed + 1
            guesses = guesses - 1
            data_entry(word)

            guessed_letters.append(word)
            print(guesses, "more")
            word = input("Input another letter: ").upper()
            self.guess_word()
            self.run()


style1 = Style(color="blue", bold=True)
style2 = Style(bold=True, color="magenta")
console.print("WELCOME TO MY HANGMAN GAME ", style=style1)
console.print("It's a guessing game. \nYou are to guess a word based on the number of blank spaces ", style=style2)
print("You have", guesses, "guesses")
t_word = target_word()
display = "_" * len(t_word)
console.print("The length of the word is", display, style="dim cyan")

word = input("Input a letter(To end, enter '!'):").upper()
