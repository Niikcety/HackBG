def chain(iterable_one, iterable_two):
    new_it = [*iterable_one, *iterable_two]
    for it in new_it:
        yield it


def compress(iterable, mask):
    zipped_it = tuple(zip(iterable, mask))

    for it in zipped_it:
        if it[1]:
            yield it[0]


def cycle(iterable):
    while True:
        for it in iterable:
            yield it


