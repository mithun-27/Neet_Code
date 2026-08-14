#Number of Connected Components in an Undirected Graph
"""You have an undirected graph of n nodes labeled from 0 to n - 1. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.

Return the number of connected components in the graph.


Example 1:



Input:
n = 5, edges = [[0,1],[1,2],[3,4]]

Output: 2

Example 2:



Input:
n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]

Output: 1

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= aᵢ < n
0 <= bᵢ < n
aᵢ != bᵢ
There are no repeated edges."""

#answer:
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res

#example 1 :
"""Input:


n=5
edges=[[0,1],[1,2],[3,4]]
Your Output:


2
Expected output:


2"""

#example 2 :
"""Input:


n=5
edges=[[0,1],[1,2],[2,3],[3,4]]
Your Output:


1
Expected output:


1"""

"""Walkthrough:
1. We want to find the number of connected components in an undirected graph. A connected component is a group of nodes where every node can be reached from every other node in that group.
2. We first build an adjacency list from the given edges. For every edge `[a, b]`, we add `b` to the neighbors of `a` and `a` to the neighbors of `b` because the graph is undirected.
3. We maintain a `visited` set to keep track of nodes that have already been explored. This prevents revisiting the same nodes multiple times.
4. We iterate through all nodes from `0` to `n - 1`. Whenever we encounter a node that has not been visited, we have found a new connected component.
5. We start a DFS or BFS from that node and mark it as visited. During the traversal, we visit all nodes that are directly or indirectly connected to it.
6. Every neighboring node that has not yet been visited is added to the DFS/BFS traversal and marked as visited.
7. Once the traversal finishes, all nodes belonging to the current connected component have been explored.
8. We increment the connected component count and continue checking the remaining nodes. If a node is already visited, it belongs to a component that has already been counted.
9. After processing all nodes, the component count represents the total number of connected components in the graph. The time complexity is `O(V + E)`, where `V` is the number of nodes and `E` is the number of edges, because every node and edge is visited at most once. The auxiliary space complexity is `O(V + E)` for the adjacency list and visited set."""