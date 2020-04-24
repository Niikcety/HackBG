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


def deep_find_all_dfs(data, key, result=[]):
    for k, v in data.items():
        if k is key:
            result.append(v)
        if isinstance(v, dict):
            deep_find_all_dfs(v, key, result)
        elif isinstance(v, list):
            for neighbour in v:
                if isinstance(neighbour, dict):
                    deep_find_all_dfs(neighbour, key, result)
    return result
