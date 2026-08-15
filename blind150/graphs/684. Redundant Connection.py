#684. Redundant Connection
"""In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected."""

#answer:
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


"""Walkthrough:
1. We are given a graph that started as a tree and then had one extra edge added. Our goal is to find the edge that creates a cycle, also known as the redundant connection.
2. We use the Disjoint Set Union (DSU) / Union-Find data structure to efficiently track which nodes belong to the same connected component.
3. We initialize two arrays: `par`, where each node is initially its own parent, and `rank`, which stores the size of each component.
4. The `find()` function is used to determine the ultimate parent (representative) of a node. It uses path compression to make future searches faster by shortening the paths in the tree.
5. The `union()` function attempts to connect two nodes. First, it finds the parent of both nodes using the `find()` function.
6. If both nodes already have the same parent, they are already connected. Adding this edge would create a cycle, so `union()` returns `False`.
7. If the nodes belong to different components, we merge them using union by rank. The smaller component is attached to the larger component, and the rank (size) is updated accordingly.
8. We process the edges one by one. For each edge `[n1, n2]`, we call `union(n1, n2)`. If `union()` returns `False`, it means this edge connects two nodes that are already in the same component and therefore creates a cycle.
9. The first edge that causes `union()` to fail is the redundant connection, so we immediately return that edge. The time complexity is approximately `O(E × α(N))`, where `α(N)` is the inverse Ackermann function (nearly constant), making the algorithm very efficient. The auxiliary space complexity is `O(N)` for the parent and rank arrays."""