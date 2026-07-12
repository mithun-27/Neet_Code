#105. Construct Binary Tree from Preorder and Inorder Traversal
"""Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree."""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head
        i, j, n = 0, 0, len(preorder)
        while i < n and j < n:
            # Go right and then as far left as possible
            curr.right = TreeNode(preorder[i], right = curr.right)
            curr = curr.right
            i += 1
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i += 1
            j += 1
            while curr.right and j < n and curr.right.val == inorder[j]:
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1
        
        return head.right
    
#example 1:
"""Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]"""
#example 2:
"""Input: preorder = [-1], inorder = [-1]
Output: [-1]"""
#example 3:
"""Input: preorder = [1,2], inorder = [2,1]
Output: [1,2]"""

"""walkthrough:
1. Create a dummy head node to simplify tree construction.
2. Initialize pointers for preorder and inorder traversals. 
3. Iterate through the preorder list, creating right child nodes for each value.
4. For each node, check if its value matches the current inorder value. If not, create left child nodes until a match is found.
5. Once a match is found, backtrack to the parent node and continue the process until all nodes are processed.
6. Return the right child of the dummy head as the root of the constructed tree.
7. The algorithm runs in O(n) time complexity, where n is the number of nodes in the tree, and uses O(n) space for the recursion stack in the worst case.
"""