"""Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root

        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right

        return -1
    
#example usage
# Create a binary tree:
# Tree:        3
#             / \
#            1   4
#             \
#              2
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
solution = Solution()
print(solution.kthSmallest(root, 1))  # Output: 1

# Create a binary tree:
# Tree:        5
#             / \
#            3   6
#           / \
#          2   4
#         /
#        1
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
solution = Solution()
print(solution.kthSmallest(root, 3))  # Output: 3

"""walkthrough
1. Initialize a variable `curr` to the root of the tree.
2. While `curr` is not null:
   a. If `curr` does not have a left child:
      i. Decrement `k` by 1.
      ii. If `k` is 0, return the value of `curr`.
      iii. Move `curr` to its right child.
   b. If `curr` has a left child:
      i. Find the predecessor of `curr` in the left subtree (the rightmost node in the left subtree).
      ii. If the predecessor's right child is null:
         - Set the predecessor's right child to `curr`.
         - Move `curr` to its left child.
      iii. If the predecessor's right child is `curr`:
         - Set the predecessor's right child to null (restore the tree).
         - Decrement `k` by 1.
         - If `k` is 0, return the value of `curr`.
         - Move `curr` to its right child.
3. If the loop ends without returning, return -1 (this should not happen if k is valid).
This algorithm uses Morris Traversal to achieve O(1) space complexity while finding the kth smallest element in the BST. The time complexity is O(n) in the worst case, where n is the number of nodes in the tree."""