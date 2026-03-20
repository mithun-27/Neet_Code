#124. Binary Tree Maximum Path Sum
"""A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
    
#example usage
# Create a binary tree:
# Tree:        -10
#             /  \
#            9   20
#               /  \
#              15   7
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution = Solution()
print(solution.maxPathSum(root))  # Output: 42


"""walkthrough
1. We define a helper function `dfs` that takes a node as input and returns the maximum path sum starting from that node and extending downwards.
2. If the current node is `None`, we return 0, as there are no paths to consider.
3. We recursively call `dfs` on the left and right children of the current node to get the maximum path sums from the left and right subtrees.
4. We take the maximum of the left and right path sums and compare it with 0 to ensure that we only consider positive contributions to the path sum. If the path sum from either subtree is negative, we treat it as 0.
5. We update the global maximum path sum `res[0]` by considering the path that goes through the current node and both left and right subtrees.
6. Finally, we return the maximum path sum that can be extended from the current node to either the left or right subtree, which is the value of the current node plus the maximum of the left and right path sums.
7. We call the `dfs` function starting from the root node and return the global maximum path sum stored in `res[0]`.
This approach ensures that we consider all possible paths in the binary tree and efficiently compute the maximum path sum. The time complexity of this solution is O(n), where n is the number of nodes in the tree, as we visit each node once. The space complexity is O(h), where h is the height of the tree, due to the recursive call stack. In the worst case, for a skewed tree, this could be O(n)."""