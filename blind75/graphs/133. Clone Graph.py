#133. Clone Graph
"""Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""

#answer
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        oldToNew[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[cur].neighbors.append(oldToNew[nei])

        return oldToNew[node]
    
#example usage
"""
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
"""

"""walkthrough
1. We start by checking if the input node is None. If it is, we return None since there is nothing to clone.    
2. We create a dictionary called oldToNew to keep track of the mapping between the original nodes and their corresponding cloned nodes. We initialize it with the input node as the key and a new Node with the same value as the value. This means that we have already cloned the input node.
3. We use a queue (deque) to perform a breadth-first traversal of the graph. We start by adding the input node to the queue.
4. We enter a loop that continues until the queue is empty. In each iteration, we pop a node from the front of the queue and process its neighbors.
5. For each neighbor of the current node, we check if it has already been cloned (i.e., if it is in the oldToNew dictionary). If it has not been cloned, we create a new Node with the same value as the neighbor and add it to the oldToNew dictionary. We also add the neighbor to the queue for further processing.
6. After ensuring that the neighbor has been cloned, we append the cloned neighbor to the neighbors list of the cloned current node (which we can access through oldToNew[cur]).
7. Once the queue is empty, we have cloned all the nodes and their relationships. We return the cloned node corresponding to the input node, which is oldToNew[node].
This approach efficiently clones the graph using a breadth-first traversal and a dictionary to keep track of the cloned nodes, resulting in a time complexity of O(N) where N is the number of nodes in the graph. The space complexity is also O(N) due to the dictionary and the queue used for traversal.
8. The example usage demonstrates how to use the Solution class to clone a graph represented as an adjacency list, and the expected output is shown in the comments.    
"""