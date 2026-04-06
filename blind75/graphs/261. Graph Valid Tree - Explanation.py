#261. Graph Valid Tree - Explanation
"""Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
Example 2:

Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false
Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2"""

#answer
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
    
#example usage
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(Solution().validTree(n, edges))  # Output: true   
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(Solution().validTree(n, edges))  # Output: false  


"""walkthrough
1. We can use a Disjoint Set Union (DSU) data structure to keep track of connected components in the graph. The DSU will help us determine if adding an edge creates a cycle and if all nodes are part of a single connected component.     
2. We first check if the number of edges is greater than n - 1. If it is, we can immediately return false, since a tree with n nodes must have exactly n - 1 edges.     
3. We initialize the DSU with n nodes and iterate through each edge. For each edge, we attempt to union the two nodes. If the union operation returns false, it means that the two nodes are already in the same component, which indicates a cycle, and we return false.
4. After processing all edges, we check if the number of components in the DSU is 1. If it is, it means all nodes are connected and we have a valid tree, so we return true. Otherwise, we return false.
5. This approach ensures that we are checking both conditions for a valid tree: no cycles and all nodes are connected.
6. The time complexity of this solution is O(n + m), where n is the number of nodes and m is the number of edges, due to the union-find operations and the initial edge count check. The space complexity is O(n) for the DSU data structure.       
"""