#102. Binary Tree Level Order Traversal
"""Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res
    
#example usage
# Create a binary tree:
# Tree:        3
#             / \
#            9   20
#               /  \
#              15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution = Solution()
print(solution.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]

"""walkthrough
1. We initialize an empty list `res` to store the final level order traversal result.
2. We use a queue (implemented as a deque) to perform a breadth-first search (BFS) on the tree. We start by adding the root node to the queue.
3. We enter a while loop that continues until the queue is empty. Inside the loop, we determine the number of nodes at the current level by checking the length of the queue (`qLen`).
4. We initialize an empty list `level` to store the values of the nodes at the current level.
5. We then iterate `qLen` times, popping nodes from the queue one by one. For each node, if it is not null, we add its value to the `level` list and enqueue its left and right children (even if they are null).
6. After processing all nodes at the current level, if the `level` list is not empty, we add it to the `res` list.
7. Finally, we return the `res` list, which contains the level order traversal of the tree.
7. The time complexity of this algorithm is O(n), where n is the number of nodes in the tree, since we visit each node exactly once. The space complexity is also O(n) in the worst case, when the tree is completely unbalanced (e.g., a linked list). In a balanced tree, the space complexity would be O(w), where w is the maximum width of the tree (the maximum number of nodes at any level)."""