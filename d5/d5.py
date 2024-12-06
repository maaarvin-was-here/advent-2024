import os

def process(f):
    rules = []
    updates = []
    finished_rules = False
    with open(f, "r") as file:
        for line in file:
            if line == '\n':
                finished_rules = True
            elif not finished_rules:
                rules.append(line.replace("\n", ""))
            else:
                updates.append(line.replace("\n", ""))
        return [rules, updates]


# build adjacency list for topo sort
def build_dependency_graph(rules):
    d_graph = {}

    for rule in rules:
        must_occur_before = rule[0]
        can_occur_after = rule[1]
        if must_occur_before not in d_graph:
            d_graph[must_occur_before] = []
        d_graph[must_occur_before].append(can_occur_after)

    return d_graph


# recursion for topo sort
def topo_helper(cur, d_graph, seen, topo_stack):
    seen.add(cur)

    if cur in d_graph:
        for i in d_graph[cur]:
            if i not in seen:
                topo_helper(i, d_graph, seen, topo_stack)

    topo_stack.append(cur)


# topo sorts a list of rules. takes list of rules and returns a hamiltonian order for those rules
def topo_sort(rules):
    d_graph = build_dependency_graph(rules)
    topo_stack = []

    visited = set()

    for node in d_graph:
        if node not in visited:
            topo_helper(node, d_graph, visited, topo_stack)
    
    s = []
    for i in topo_stack:
        s.insert(0, i)

    return(s)


def d5(rules, updates):

    # for each update, use only the rules that pertain to that update (both values of the rule is included in the update)
    per_rules = {}
    for update in updates:
        for rule in rules:
            if all(v in update for v in rule):
                if per_rules.get(tuple(update)) == None:
                    per_rules[tuple(update)] = []
                per_rules[tuple(update)].append(rule)

    sol_1 = 0
    sol_2 = 0

    for update in updates:
        s = topo_sort(per_rules[tuple(update)])
        if s == update:
            sol_1 += update[len(s)//2]
        else:
            sol_2 += s[len(s)//2]
    
    return sol_1, sol_2
    
    
        

if __name__ == '__main__':
    input_file = '{}/d5.txt'.format(os.path.basename(__file__).split(".")[0])
    list = process(input_file)

    rule_input = [[int(x) for x in line.split("|")] for line in list[0]]
    updates_input = [[int(x) for x in line.split(",")] for line in list[1]]

    p1, p2 = d5(rule_input, updates_input)
    
    print(p1)
    print(p2)
    
'''
    for u in updates:
        for rule in rules
        '''
'''


alid_updates = []
    for u in updates:
        update = u.split(",")
        print(update)
        indices = []
        for char in update:
            indices.append(topo.index(char))
        print(indices)
        print(" ")
        print(update)
        valid = True
        for i in range(1, len(update)):
            update[i]
            print(topo.index(update[i]))
            print(topo.index(update[i-1]))
            if topo.index(update[i]) < topo.index(update[i-1]):
                valid = False
        if valid:
            valid_updates.append(update)
            print("[VALID]")
        else:
            print("[NOT VALID]!")

    print("valid")
    print(valid_updates)

'''