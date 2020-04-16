import random


def letter_generator():
    return chr(random.randint(0, 25) + 97)


def word_generator():
    word = ""
    length = random.randint(3, 15)
    for i in range(length):
        word += letter_generator()

    return word


