import networkx


with open('input.txt') as f:
    tree = networkx.DiGraph()
    for line in f.readlines():
        name = line.split()[0]
        tree.add_node(name, weight=int(line.split()[1].strip('()')))

        if '->' in line:
            line = line.split('->')[1].split(',')
            sub_tower = [x.strip() for x in line]

            for tower in sub_tower:
                tree.add_edge(name, tower)

    solution = list(networkx.topological_sort(tree))

    print(solution[0])
