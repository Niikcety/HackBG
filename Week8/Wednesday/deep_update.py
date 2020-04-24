root = {
    'A': 1,
    'B': {
        'C': {
            'K': {
                'K': 10,
                'L': 15,
                'Z': 20},
            'E': 7},
        'F': 3},
    'K': 100}


def deep_update(data, key, value):
    for k, v in data.items():
        print('{}:{}'.format(k, v))
        if k is key:
            data[k] = value
        if isinstance(v, dict):
            deep_update(v, key, value)
        elif isinstance(v, list):
            for neighbour in v:
                if isinstance(neighbour, dict):
                    deep_update(neighbour, key, value)
    return data
