#Graph Valid Tree
"""Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.


Example 1:



Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]

Output: true

Example 2:



Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]

Output: false

Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= a_i, b_i < n
a_i != b_i
There are no self-loops or repeated edges."""

#answer:
class DSU:
    def __init__(self, n):
        self.comps = n
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False

        self.comps -= 1
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

    def components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return dsu.components() == 1


#example 1 :
"""Input:


n=5
edges=[[0,1],[0,2],[0,3],[1,4]]
Your Output:


true
Expected output:


true"""

#example 2 :
"""Input:


n=5
edges=[[0,1],[1,2],[2,3],[1,3],[1,4]]
Your Output:


false
Expected output:


false"""


"""Walkthrough:
1. We want to determine whether the given undirected graph forms a valid tree. A valid tree must satisfy two conditions: it must be fully connected, and it must not contain any cycles.
2. We first build an adjacency list to represent the graph, where each node stores its neighboring nodes.
3. We use a Depth-First Search (DFS) or Breadth-First Search (BFS) starting from node `0` to explore the graph.
4. During the traversal, we maintain a visited set to keep track of nodes that have already been explored. Since the graph is undirected, we also keep track of the parent node to avoid treating the edge back to the parent as a cycle.
5. While visiting a node, if we encounter a neighbor that has already been visited and is not the parent of the current node, a cycle exists. In this case, the graph cannot be a valid tree, so we return `False`.
6. If the traversal completes without detecting a cycle, we then check whether all `n` nodes have been visited.
7. If some nodes were not visited, the graph is disconnected, meaning there are multiple components. A disconnected graph cannot be a valid tree, so we return `False`.
8. If there is no cycle and every node is reachable from the starting node, the graph is connected and acyclic, which satisfies the definition of a tree.
9. The algorithm returns `True` only when both conditions are met. The time complexity is `O(V + E)`, where `V` is the number of nodes and `E` is the number of edges, because every node and edge is visited at most once. The auxiliary space complexity is `O(V + E)` for the adjacency list, visited set, and recursion stack or queue."""