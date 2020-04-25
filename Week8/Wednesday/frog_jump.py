lake = ['>', '>', '>', '_', '<', '<', '<']


def generate_swamp(n):
    lfrog = (n // 2) * '>'
    rfrog = (n // 2) * '<'
    return lfrog + '_' + rfrog



def generate_tree(swamp, tree={}):
    l_swamp = list(swamp)
    l_pos = l_swamp.index('_')
    # One left
    if l_pos == 0:
        smp_tmp = l_swamp[:]
        if smp_tmp[1] == '<':
            smp_tmp[0], smp_tmp[1] = smp_tmp[1], smp_tmp[0]
            swamp_tmp = ''.join(smp_tmp)
            tree[swamp_tmp] = dict()
            generate_tree(swamp_tmp, tree[swamp_tmp])
        elif smp_tmp[2] == '<':
            smp_tmp[0], smp_tmp[2] = smp_tmp[2], smp_tmp[0]
            swamp_tmp = ''.join(smp_tmp)
            tree[swamp_tmp] = dict()
            generate_tree(swamp_tmp, tree[swamp_tmp])
        return
    elif l_pos == (len(l_swamp) - 1):
        smp_tmp = l_swamp[:]
        if smp_tmp[l_pos - 2] == '>':
            smp_tmp[l_pos - 2], smp_tmp[l_pos] = smp_tmp[l_pos], smp_tmp[l_pos - 2]
            swamp_tmp = ''.join(smp_tmp)
            tree[swamp_tmp] = dict()
            generate_tree(swamp_tmp, tree[swamp_tmp])
        elif smp_tmp[l_pos - 3] == '>':
            smp_tmp[l_pos - 3], smp_tmp[l_pos] = smp_tmp[l_pos], smp_tmp[l_pos - 3]
            swamp_tmp = ''.join(smp_tmp)
            tree[swamp_tmp] = dict()
            generate_tree(swamp_tmp, tree[swamp_tmp])
        return
    elif l_pos == 1:
        smp_tmp = l_swamp[:]
        if smp_tmp[l_pos - 1] == '>':
            smp_tmp[l_pos - 1], smp_tmp[l_pos] = smp_tmp[l_pos], smp_tmp[l_pos - 1]
            swamp_tmp = ''.join(smp_tmp)
            tree[swamp_tmp] = dict()
            generate_tree(swamp_tmp, tree[swamp_tmp])
        elif smp_tmp[l_pos + 1] == '<':
            smp_tmp = l_swamp[:]
            smp_tmp[l_pos + 1], smp_tmp[l_pos] = smp_tmp[l_pos], smp_tmp[l_pos + 1]
            swamp_tmp = ''.join(smp_tmp)
            tree[swamp_tmp] = dict()
            generate_tree(swamp_tmp, tree[swamp_tmp])
        elif smp_tmp[l_pos + 2] == '<':
            smp_tmp = l_swamp[:]
            smp_tmp[l_pos + 2], smp_tmp[l_pos] = smp_tmp[l_pos], smp_tmp[l_pos + 2]
            swamp_tmp = ''.join(smp_tmp)
            tree[swamp_tmp] = dict()
            generate_tree(swamp_tmp, tree[swamp_tmp])
        return
    elif l_pos == (len(l_swamp) - 2):
            smp_tmp = l_swamp[:]
            if smp_tmp[l_pos + 1] == '<':
                smp_tmp[l_pos + 1], smp_tmp[l_pos] = smp_tmp[l_pos], smp_tmp[l_pos + 1]
                swamp_tmp = ''.join(smp_tmp)
                tree[swamp_tmp] = dict()
                generate_tree(swamp_tmp, tree[swamp_tmp])
            elif smp_tmp[l_pos - 1] == '>':
                smp_tmp = l_swamp[:]
                smp_tmp[l_pos - 1], smp_tmp[l_pos] = smp_tmp[l_pos], smp_tmp[l_pos - 1]
                swamp_tmp = ''.join(smp_tmp)
                tree[swamp_tmp] = dict()
                generate_tree(swamp_tmp, tree[swamp_tmp])
            elif smp_tmp[l_pos - 2] == '>':
                smp_tmp = l_swamp[:]
                smp_tmp[l_pos - 2], smp_tmp[l_pos] = smp_tmp[l_pos], smp_tmp[l_pos - 2]
                swamp_tmp = ''.join(smp_tmp)
                tree[swamp_tmp] = dict()
                generate_tree(swamp_tmp, tree[swamp_tmp])
            return
    else:
        smp_tmp = l_swamp[:]
        if smp_tmp[l_pos - 1] == '>':
            smp_tmp[l_pos - 1], smp_tmp[l_pos] = smp_tmp[l_pos], smp_tmp[l_pos - 1]
            swamp_tmp = ''.join(smp_tmp)
            tree[swamp_tmp] = dict()
            generate_tree(swamp_tmp, tree[swamp_tmp])
        # Two left
        smp_tmp = l_swamp[:]
        if smp_tmp[l_pos - 2] == '>':
            smp_tmp[l_pos - 2], smp_tmp[l_pos] = smp_tmp[l_pos], smp_tmp[l_pos - 2]
            swamp_tmp = ''.join(smp_tmp)
            tree[swamp_tmp] = dict()
            generate_tree(swamp_tmp, tree[swamp_tmp])
        # One right
        smp_tmp = l_swamp[:]
        if smp_tmp[l_pos + 1] == '<':
            smp_tmp[l_pos + 1], smp_tmp[l_pos] = smp_tmp[l_pos], smp_tmp[l_pos + 1]
            swamp_tmp = ''.join(smp_tmp)
            tree[swamp_tmp] = dict()
            generate_tree(swamp_tmp, tree[swamp_tmp])
        # Two right
        smp_tmp = l_swamp[:]
        if smp_tmp[l_pos + 2] == '<':
            smp_tmp[l_pos + 2], smp_tmp[l_pos] = smp_tmp[l_pos], smp_tmp[l_pos + 2]
            swamp_tmp = ''.join(smp_tmp)
            tree[swamp_tmp] = dict()
            generate_tree(swamp_tmp, tree[swamp_tmp])

    return tree


def frog_jump(frogs):
    assert frogs % 2 == 0, 'Frogs should be even'
    swamp = generate_swamp(frogs)
    goal = swamp[::-1]
    tree = generate_tree(swamp)

    def find_frogs(tree, goal, visited=[]):
        for key, value in tree.items():
            visited.append(key)
            if key is goal:
                return visited
            else:
                for neighbour in value:
                    find_frogs(value[neighbour], goal, visited)
        return visited
    return find_frogs(tree, goal)


print(frog_jump(6))
