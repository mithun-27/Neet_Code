#323. Number of Connected Components In An Undirected Graph
"""You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.

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
0 <= aᵢ <= bᵢ < n
aᵢ != bᵢ
There are no repeated edges."""

#answer
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
    
#example 1:
n = 5
edges = [[0,1],[1,2],[3,4]] 
print(Solution().countComponents(n, edges)) # Output: 2
#example 2:
n = 5
edges = [[0,1],[1,2],[2,3],[3,4]]
print(Solution().countComponents(n, edges)) # Output: 1

"""walkthrough
1. We can use a Disjoint Set Union (DSU) data structure to keep track of the connected components in the graph. The DSU will allow us to efficiently union two nodes and find the representative (or parent) of a node.
2. We initialize the DSU with n nodes, where each node is its own parent and has a rank of 1.
3. We iterate through the edges and for each edge (u, v), we perform a union operation on the DSU. If the union is successful (i.e., u and v were in different components), we decrement the count of connected components.
4. Finally, we return the count of connected components, which is the initial number of nodes minus the number of successful unions.
5. The time complexity of this solution is O(n + m * α(n)), where n is the number of nodes, m is the number of edges, and α(n) is the inverse Ackermann function, which is very slow-growing and can be considered almost constant for practical purposes. The space complexity is O(n) for the DSU data structure. 
6. This approach efficiently counts the number of connected components in the graph by leveraging the properties of the DSU data structure to manage and merge components as we process the edges.  
7. The DSU implementation uses path compression in the find method and union by rank in the union method to optimize the operations, ensuring that we can handle the maximum constraints efficiently.   
8. The final result is the number of connected components in the graph, which is returned after processing all edges.   
9. This solution is efficient and works well within the given constraints, making it suitable for large graphs with up to 2000 nodes and 5000 edges.
10. The DSU class provides a clean and modular way to manage the connected components, making the main solution straightforward and easy to understand. The union and find operations are encapsulated within the DSU class, allowing us to focus on the logic of counting components in the main solution method.
"""