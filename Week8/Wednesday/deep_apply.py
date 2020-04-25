root = {
    'A': 1,
    'B': {
        'C': {
            'D': {
                'K': 10,
                'L': 15,
                'Z': 20},
            'E': 7},
        'F': 3},
    'K': 100}


def deep_apply(func, data):
    for k, v in data.items():
        data[func(k)] = data.pop(k)
        if isinstance(v, dict):
            deep_apply(func, v)
        elif isinstance(v, list):
            for neighbour in v:
                if isinstance(v, dict):
                    deep_apply(func, neighbour)
    return data


def a_adder(key):
    key += 'A'
    return key


print(deep_apply(a_adder, root))
