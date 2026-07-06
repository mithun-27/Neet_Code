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
p and q will exist in the BST."""

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
            

#example 1
""" Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6. """
#example 2
""" Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2   
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition. """
#example 3
""" Input: root = [2,1], p = 2, q = 1
Output: 2
Explanation: The LCA of nodes 2 and 1 is 2. """ 


"""walkthrough:
1. Start at the root of the BST.
2. Compare the values of p and q with the current node's value. 
3. If both p and q are greater than the current node's value, move to the right child of the current node.
4. If both p and q are less than the current node's value, move to the left child of the current node.
5. If one of p or q is less than the current node's value and the other is greater than the current node's value, then the current node is the lowest common ancestor (LCA) of p and q. Return the current node.
6. Repeat steps 2-5 until the LCA is found or the end of the tree is reached. If the end of the tree is reached without finding the LCA, return None.   
7. The time complexity of this algorithm is O(h), where h is the height of the BST. In the worst case, the height of the BST can be equal to the number of nodes in the tree, resulting in a time complexity of O(n). However, in a balanced BST, the height is logarithmic with respect to the number of nodes, resulting in a time complexity of O(log n). The space complexity is O(1) since we are using a constant amount of space for variables and not using any additional data structures. 
8. The algorithm is efficient and works well for large BSTs, as it only traverses the tree once and does not require any additional data structures. It is also easy to implement and understand, making it a good choice for solving the LCA problem in a BST."""