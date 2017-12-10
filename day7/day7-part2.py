import networkx
import collections


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

weights = {}

for disc in reversed(solution):
    total = tree.nodes[disc]['weight']

    counts = collections.Counter(weights[sub_disc] for sub_disc in tree[disc])
    unbalanced = None

    for sub_disc in tree[disc]:
        if len(counts) > 1 and counts[weights[sub_disc]] == 1:
            unbalanced = sub_disc
            break

        val = weights[sub_disc]
        total += weights[sub_disc]

    if unbalanced:
        diff = weights[unbalanced] - val
        print(tree.nodes[unbalanced]['weight'] - diff)
        break

    weights[disc] = total
