#98. Validate Binary Search Tree
"""Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True
    
#example usage
# Create a binary tree:
# Tree:        2
#             / \
#            1   3
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
solution = Solution()
print(solution.isValidBST(root))  # Output: True

# Create a binary tree:
# Tree:        5
#             / \
#            1   4
#               / \
#              3   6
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)   
root.right.right = TreeNode(6)
solution = Solution()
print(solution.isValidBST(root))  # Output: False

"""walkthrough:
1. We start by checking if the root is None. If it is, we return True since an empty tree is a valid BST.
2. We initialize a queue (using deque) to perform a breadth-first traversal of the tree. We start by adding the root node along with its valid range (negative infinity to positive infinity) to the queue.
3. We enter a loop that continues until the queue is empty. In each iteration, we pop a node from the queue along with its valid range (left and right).
4. We check if the current node's value is within the valid range (left < node.val < right). If it is not, we return False since the BST property is violated.
5. If the current node has a left child, we add it to the queue with an updated valid range (left, node.val) since all values in the left subtree must be less than the current node's value.
6. If the current node has a right child, we add it to the queue with an updated valid range (node.val, right) since all values in the right subtree must be greater than the current node's value.
7. If we finish processing all nodes without finding any violations of the BST property, we return True.    
"""