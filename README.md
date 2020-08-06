# Estimating Graduation Time

When pursuing a degree, a student needs to complete a number of credits in order to graduate. Credits are accumulated as the student takes various courses, some core courses, some elective. Except for a few courses, each other course has a number of course prerequisites that need to be taken before the respective course can be taken. 

For example, at California State University in Computer Science, in order for a student to graduate with a BS in CS, the students need to accumulate at least 120 credits, out of which 18 credits (i.e. 6 courses) are elective and the rest of 102 belong to core courses. In the below figure, core courses are drawn as a directed graph. 
(For additional course related details, see the [undergraduate handbook][1])

![Figure 1](https://imgur.com/RD1m793.png)

We ignore the graphs on the right side and we focus only on the graphs on the left and center; that graph is a DAG. The problem requires computing how many semesters a student needs in order to graduate. This translates into computing the longest path in the DAG, since the number of hops on the longest path corresponds to the number of semesters needed to graduate. We ignore that there is a limit on the number of courses a student needs to take in any given semester. Before we compute the longest path, the problem requires re-labeling the nodes using topological sorting and using values in the range *0 ... N-1*.

# Topological Sorting

The directed graph `G = (V, E)` is given in a text file called ​`input.txt​` in which the first row contains the number of nodes `N`, the second row contains the `#` sign, and the next `N` rows contain the `IDs` of the nodes in some order, followed by a row with the `#` sign, followed by all the arcs. Each arc is a pair of two IDs, separated by space. Each ID is a string of maximum 8 characters. An example of such a file `​input.txt​` is below, and the corresponding DAG is as shown int he below figure:

![Figure 2](https://imgur.com/Crt3cER.png)

The set of edges is read from the file as an edge list, another approach is to use a *0-1 adjacency matrix*. Recall that a *0-1 adjacency matrix* is a square matrix of size `NxN` where N is the number of nodes, and each element is either 0 or 1:

`A[i][j] = 1` if and only if there is an arc from node `i` to node `j`

We would like the nodes to be renumbered from `0 ...N-1` such that if `(i,j)` is an arc from `i` to `j`, then `i < j`. The topological sort will give an order in which courses need to be taken.

# Longest Path in a Directed Acyclic Graph

The longest path problem is the problem of finding a simple path of maximal length in a DAG, i.e. among all possible simple paths in the DAG, the problem is to find the longest one. Since we assume that the DAG is unweighted, it suffices to find the longest path in terms of the number of edges.

For a general graph, computing the longest path is NP-hard (exponential) solution. Well, why not simply enumerate all the paths, and find the longest one? Because, there can be exponentially many such `n` paths! 

For example in the below figure, there are 2​ different paths from vertex `1` to `n`, so computing the longest one takes exponential time.

![Figure 3](https://i.imgur.com/TLiILXZ.png)

Fortunately, the longest path in a DAG does have optimal substructure, which allows us to solve it using dynamic programming. 

# Output

The output displays the list of nodes in topological sorting, separated by whitespace (space, tab, new line, etc.) followed by a new line, then followed by the length of the longest path and a longest path.

For example, for the graph in the second figure, the output will be:

```
Topological sorting:
C2  A1  C1  B2  B1  A2

Length of the longest path:
2

A longest path:
A1  C1  B2
```

[1]: http://www.fullerton.edu/ecs/cs/_resources/pdf/CPSC_undergraduate_handbook-2018-19.pdf​.
