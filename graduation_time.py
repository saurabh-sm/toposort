import os
from collections import defaultdict

def parse_files():
    """
    Read all input files into variables of nodes and edges.
    """
    text_files = [filename for filename in os.listdir(os.getcwd()) if filename.endswith('.txt')]
    graphs = []
    for file in text_files:
        graph_content = []
        with open (file, 'rt') as graph_input:
            for lines in graph_input:
                graph_content.append(lines.strip('\n'))
        graphs.append(graph_content)
    return graphs


def create_graph(graph_content):
    """
    Read each line from the file into a list. First line in the file contains
    the number of nodes. Nodes are between #, which is on line 2 and line
    "_number_of_nodes_" + 1. From this point onwards, the file contains a
    list of connected edges.
    Create a dictionary to represent nodes and edges. Each node has a list of
    edges.
    """
    graph_nodes = graph_content[2: int(graph_content[0]) + 2]
    graph_edges = graph_content[int(graph_content[0]) + 3 : ]
    nested_graph_edges = [[element] for element in graph_edges]
    split_edges = [i[0].split() for i in nested_graph_edges]

    edge_pair = [edge.strip().split(' ') for edge in graph_edges]
    graph_dict = {key: [] for key in graph_nodes}
    for a,b in edge_pair:
        graph_dict[a].append(b)

    return graph_dict, split_edges


def topological_sort(graph, start):
    """
    Implementation of DFS topological sort
    """
    seen = set()
    stack = []; order = []
    q = [start]
    while q:
        v = q.pop()
        if v not in seen:
            seen.add(v)
            q.extend(graph[v])
            while stack and v not in graph[stack[-1]]:
                order.append(stack.pop())
            stack.append(v)
    return stack + order[::-1]


def DFS(G,v,seen=None,path=None):
    """
    Path trace in graph 'G', starting from vertex 'v'
    """
    if seen is None: seen = []
    if path is None: path = [v]
    seen.append(v)
    paths = []
    for traverse in G[v]:
        if traverse not in seen:
            t_path = path + [traverse]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, traverse, seen[:], t_path))
    return paths


def longest_path(edges):
    # Define graph by edges, and build graph dictionary
    G = defaultdict(list)
    for (s,t) in edges:
        G[s].append(t)
        G[t].append(s)

    vertex_longest = DFS(G, '1')     # compute longest path from vertex 'v'

    # compute longest path between any two points
    all_longest = []
    for node in set(G.keys()):
        for path in DFS(G, node):
            all_longest.append(path)

    max_len   = max(len(path) for path in vertex_longest)
    max_paths = [path for path in vertex_longest if len(path) == max_len]

    print("\nLength of the longest path:")
    print(max_len)

    print("\nLongest Paths:")
    for path in max_paths:
        print(path)


def main():
    graph1, graph2, graph3 = parse_files()
    created_graph, edge_pairs = create_graph(graph1)
    starting_index = '2'
    print("Created graph: ")
    print(created_graph)
    print("\nEdge pairs: ")
    print(edge_pairs)
    print("\nTopological sorting:")
    print(topological_sort(created_graph, starting_index))
    longest_path(edge_pairs)


if __name__ == '__main__':
    main()
