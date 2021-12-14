from collections import defaultdict
from collections import Counter

def parse_input(input):    
    graph = defaultdict(list)
    for edge in input:
        # print('--{}'.format(edge))
        a,b = edge.split('-')
        graph[a].append(b)
        graph[b].append(a)

    return graph

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        counts = path
        paths = []
        for node in graph[start]:
            # if node not in path or node.isupper():
            if (counts.count(node)<2 and node!='start') or node.isupper():
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def main():
    
    example = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".splitlines()

    example2="""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".splitlines()


    with open("input.txt") as infile:
        input = [line.strip() for line in infile]
    
    graph  = parse_input(example)



    paths = find_all_paths(graph, 'start', 'end')

    print('paths:{}'.format(len(paths)))


if __name__ == '__main__':
    main()