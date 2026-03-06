#226. Invert Binary Tree
"""Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from sympy import root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
    
#example usasge
# Create a binary tree:        4
#                            /   \
#                           2     7
#                          / \   / \
#                         1   3 6   9
# Invert the binary tree
# The inverted tree will be:   4
#                            /   \
#                           7     2
#                          / \   / \
#                         9   6 3   1
Solution().invertTree(root)


"""walkthrough
1. Check if the root is None. If it is, return None.
2. Initialize a stack with the root node.
3. While the stack is not empty:
   a. Pop a node from the stack.
   b. Swap the left and right children of the node.
   c. If the left child exists, push it onto the stack.
   d. If the right child exists, push it onto the stack.
4. Return the root of the inverted tree.
The time complexity of this algorithm is O(n), where n is the number of nodes in the binary tree, because we visit each node exactly once. The space complexity is O(h), where h is the height of the tree, due to the stack used for depth-first traversal. In the worst case (a completely unbalanced tree), the space complexity can be O(n)."""