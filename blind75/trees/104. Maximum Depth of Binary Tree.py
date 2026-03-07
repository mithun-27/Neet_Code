#104. Maximum Depth of Binary Tree
"""Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
    
#example usage
# Create a binary tree:        3
#                            /   \
#                           9     20
#                                /  \
#                               15   7
# Get the maximum depth of the binary tree
# The maximum depth will be 3, as the longest path from the root to a leaf node is 3 -> 20 -> 15 or 3 -> 20 -> 7.
# Create a binary tree:        1
#                             \
#                              2
# Get the maximum depth of the binary tree
# The maximum depth will be 2, as the longest path from the root to a leaf node is 1 -> 2.

"""walkthrough
To find the maximum depth of a binary tree, we can use a breadth-first search (BFS) approach. We will utilize a queue to traverse the tree level by level.  
1. We start by initializing a queue and adding the root node to it if it is not null.
2. We also initialize a variable `level` to keep track of the current depth of the tree.
3. We then enter a loop that continues until the queue is empty. Inside the loop, we iterate through all the nodes at the current level (using the length of the queue to determine how many nodes are at that level).
4. For each node at the current level, we check if it has left and right children. If it does, we add those children to the queue for processing in the next iteration.
5. After processing all nodes at the current level, we increment the `level` variable to indicate that we have moved down one level in the tree.
6. Once the queue is empty, we have traversed all levels of the tree, and the `level` variable will contain the maximum depth of the binary tree, which we return as the result.    
"""