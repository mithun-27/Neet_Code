#230. Kth Smallest Element in a BST
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
    
#example 1:
"""Input: root = [3,1,4,null,2], k = 1
Output: 1"""
#example 2:
"""Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3"""
#example 3:
"""Input: root = [1], k = 1
Output: 1"""

"""walkthrough:
1. To find the kth smallest element in a binary search tree (BST), we can perform an in-order traversal of the tree, which visits the nodes in ascending order.
2. We can use a stack to simulate the in-order traversal iteratively. We start from the root node and push all the left children onto the stack until we reach a null node.
3. Once we reach a null node, we pop the top node from the stack, which represents the next smallest element in the BST. We decrement k by 1, and if k becomes 0, we return the value of the current node as the kth smallest element.
4. If k is not 0, we move to the right child of the current node and repeat the process of pushing left children onto the stack.
5. We continue this process until we find the kth smallest element or exhaust all nodes in the BST. If we reach the end of the traversal without finding the kth smallest element, we return -1 as an indication that k is out of bounds.           
6. The time complexity of this approach is O(h + k), where h is the height of the tree, as we may need to traverse down to the leftmost node and then visit k nodes. The space complexity is O(h) for the stack used in the traversal, where h is the height of the tree. In the worst case, for a skewed tree, the space complexity can be O(n), but for a balanced tree, it will be O(log n)."""