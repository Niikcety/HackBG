import random


def letter_generator():
    return chr(random.randint(0, 25) + 97)


def word_generator():
    word = ""
    length = random.randint(3, 15)
    for i in range(length):
        word += letter_generator()

    return word


def chapter_generator(words):
    counter = 0
    chapter = ''
    while(counter < words):
        chapter += word_generator() + ' '
        if random.randint(0, 20) > 17:
            chapter += '\n'
        counter += 1
    yield chapter


def book_generator(chapters_count, chapter_length, name_of_book='MyBook'):
    with open('MyBook.txt', 'w') as f:
        for i in range(1, chapters_count + 1):
            f.write(f'# Chapter {i} \n')
            f.write(next(chapter_generator(chapter_length)))
            f.write('\n \n')
