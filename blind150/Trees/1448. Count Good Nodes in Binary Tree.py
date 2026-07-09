#1448. Count Good Nodes in Binary Tree
"""Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4]."""

#example 1:
"""Input: root = [3,1,4,3,null,1,5]
Output: 4"""
#example 2:
"""Input: root = [3,3,null,4,2]
Output: 3"""
#example 3:
"""Input: root = [1]
Output: 1"""

"""walkthrough:
1.We can use a depth-first search (DFS) approach to traverse the binary tree and keep track of the maximum value encountered along the path from the root to the current node.
2. We can define a recursive function that takes the current node and the maximum value encountered so far as parameters. If the current node's value is greater than or equal to the maximum value, we increment a counter for good nodes and update the maximum value.
3. We then recursively call the function for the left and right children of the current node, passing the updated maximum value along the path. Finally, we return the count of good nodes after traversing the entire tree.    
4. The time complexity of this approach is O(n), where n is the number of nodes in the binary tree, as we visit each node once. The space complexity is O(h), where h is the height of the tree, due to the recursive call stack.   
5. The space complexity can be O(n) in the worst case for a skewed tree, but it will be O(log n) for a balanced tree. 
"""