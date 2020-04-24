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


def deep_find_dfs(data, key):
    for k, v in data.items():
        if key is k:
            return v
        if isinstance(v, dict):
            return deep_find_dfs(v, key)
        elif isinstance(v, list):
            for neighbour in v:
                if isinstance(neighbour, dict):
                    return deep_find_dfs(neighbour, key)
