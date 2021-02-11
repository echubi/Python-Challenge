import random

file = "data\\words.txt"

words = [line.rstrip('\n') for line in open(file)]


def target_word():
    a = random.choice(words)
    return a.upper()
