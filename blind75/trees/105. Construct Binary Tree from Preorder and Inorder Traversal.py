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
    
#example usage
# Create a binary tree:
# Tree:        3
#             / \
#            9  20
#              /  \
#             15   7
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solution = Solution()
result = solution.buildTree(preorder, inorder)
# The result is the root of the constructed binary tree. You can perform a traversal to verify the structure of the tree.

"""walkthrough
1. We start by creating a dummy head node and a pointer `curr` that initially points to this dummy node. We also initialize two pointers `i` and `j` to keep track of our position in the `preorder` and `inorder` lists, respectively.
2. We enter a loop that continues until we have processed all nodes in the `preorder` list. Inside the loop, we first create a new node with the value from the `preorder` list at index `i` and set it as the right child of `curr`. We then move `curr` to this new node and increment `i` to move to the next value in the `preorder` list.
3. Next, we enter another loop that continues as long as the value of `curr` does not match the value at index `j` in the `inorder` list. Inside this loop, we create a new node with the value from the `preorder` list at index `i` and set it as the left child of `curr`. We then move `curr` to this new node and increment `i`.
4. Once we exit the inner loop, we increment `j` to move to the next value in the `inorder` list. We then enter another loop that continues as long as the right child of `curr` exists and its value matches the value at index `j` in the `inorder` list. Inside this loop, we temporarily store the right child of `curr`, set the right child of `curr` to `None`, move `curr` to the temporarily stored node, and increment `j`.
5. Finally, after processing all nodes, we return the right child of the dummy head node, which is the root of the constructed binary tree. This approach effectively reconstructs the binary tree by leveraging the properties of preorder and inorder traversals. The time complexity of this algorithm is O(n) since we process each node exactly once, and the space complexity is also O(n) due to the recursive stack and the storage of nodes in the tree.   
"""