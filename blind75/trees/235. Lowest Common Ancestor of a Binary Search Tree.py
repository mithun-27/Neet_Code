#235. Lowest Common Ancestor of a Binary Search Tree
"""Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""
#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
            
#example usage
# Create a binary search tree:
# Tree:        6
#             / \
#            2   8
#           / \ / \
#          0  4 7  9
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)  
p = root.left  # Node with value 2
q = root.right  # Node with value 8
solution = Solution()
lca = solution.lowestCommonAncestor(root, p, q)
print(lca.val)  # Output: 6

"""walthrough
1. We start at the root of the BST, which is 6.
2. We compare the values of p (2) and q (8) with the current node's value (6).
3. Since p.val (2) is less than 6 and q.val (8) is greater than 6, we have found the split point where p and q diverge in the tree. This means that the current node (6) is the lowest common ancestor of p and q.
4. We return the current node (6) as the result.
The time complexity of this algorithm is O(h), where h is the height of the BST. In the worst case, if the BST is skewed, the height can be O(n), where n is the number of nodes in the tree. However, in a balanced BST, the height is O(log n), making the algorithm efficient for large trees. The space complexity is O(1) since we are using only a constant amount of extra space to store the current node."""