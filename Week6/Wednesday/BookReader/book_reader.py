import glob


def file_generator(path_to_book):
    files = glob.glob(path_to_book + '/*.txt')
    for file in files:
        yield file


def chapter_generator(file):
    file = open(file, 'r')
    line = file.readline()
    result = ''
    while line != '':
        if line[0] == '#':
            if result != '':
                yield result
                result = ''
                result += line
            else:
                result += line
        else:
            result += line
        line = file.readline()
    yield result


def book_reader(path_to_book):
    for file in file_generator(path_to_book):
        print(file)
        chapter = chapter_generator(file)
        while True:
            try:
                yield next(chapter)
            except StopIteration:
                break


book = book_reader('Book')
print(next(book))
print(next(book))
print(next(book))
print(next(book))
print(next(book))
print(next(book))
print(next(book))
print(next(book))
print(next(book))
print(next(book))
