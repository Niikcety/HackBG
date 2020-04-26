def generate_swamp(n):
    lfrog = (n // 2) * '>'
    rfrog = (n // 2) * '<'
    return lfrog + '_' + rfrog


def move_right(swamp, lily_pos, step):
    tmp_swamp = swamp[:]
    try:
        if tmp_swamp[lily_pos + step] is '<':
            tmp_swamp[lily_pos], tmp_swamp[lily_pos + step] = tmp_swamp[lily_pos + step], tmp_swamp[lily_pos]
            return ''.join(tmp_swamp)
    except IndexError:
        return None
    return None


def move_left(swamp, lily_pos, step):
    tmp_swamp = swamp[:]
    if lily_pos - step >= 0:
        try:
            if tmp_swamp[lily_pos - step] is '>':
                tmp_swamp[lily_pos - step], tmp_swamp[lily_pos] = tmp_swamp[lily_pos], tmp_swamp[lily_pos - step]
                return ''.join(tmp_swamp)
        except IndexError:
            return None
    return None


def generate_tree(swamp, tree={}):
    if swamp is None:
        return
    l_swamp = list(swamp)
    l_pos = l_swamp.index('_')
    tree[swamp] = dict()

    two_steps_left = move_left(l_swamp, l_pos, 2)
    generate_tree(two_steps_left, tree[swamp])

    one_step_left = move_left(l_swamp, l_pos, 1)
    generate_tree(one_step_left, tree[swamp])

    one_step_right = move_right(l_swamp, l_pos, 1)
    generate_tree(one_step_right, tree[swamp])

    two_steps_right = move_right(l_swamp, l_pos, 2)
    generate_tree(two_steps_right, tree[swamp])

    return tree


def find_paths(tree, path=[]):
    for key, value in tree.items():
        path.append(key)
        for neighbour in value:
            path.append(neighbour)
            find_paths(value[neighbour], path)
    return path


def find_only_correct_paths(tree, swamp, goal):
    initial_state = list(tree[swamp].keys())
    paths = find_paths(tree)
    solve_paths = []
    indexes_of_end_states = [i for i, d in enumerate(paths) if d == goal]
    for times in range(0, len(indexes_of_end_states)):
        path = []
        for i in range(indexes_of_end_states[times], 0, -1):
            path.append(paths[i])
            if paths[i] in initial_state:
                path.append(swamp)
                break
        solve_paths.append(path[::-1])

    return solve_paths


def frog_jump(frogs):
    assert frogs % 2 == 0, 'Frogs should be even'
    swamp = generate_swamp(frogs)
    goal = swamp[::-1]
    tree = generate_tree(swamp)
    solve_paths = find_only_correct_paths(tree, swamp, goal)

    for i in range(len(solve_paths)):
        print('{} Solve'.format(i + 1))
        for j in range(len(solve_paths[i])):
            print('({}): {}'.format(j + 1, solve_paths[i][j]))

    return


if __name__ == '__main__':
    frogs = int(input('Please enter number of frogs:'))
    frog_jump(frogs)
