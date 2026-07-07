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
    
#example 1
""" Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]] """
#example 2
""" Input: root = [1]
Output: [[1]] """
#example 3
""" Input: root = []
Output: [] """

"""walkthrough:
1. Initialize an empty list res to store the final result.  
2. Create a deque (double-ended queue) q and append the root node to it. This will be used for level order traversal.
3. While the queue is not empty, do the following:
   - Get the number of nodes at the current level (qLen).
   - Initialize an empty list level to store the values of nodes at the current level.
   - For each node at the current level, pop it from the queue, append its value to level, and append its children (if any) to the queue.
   - If level is not empty, append it to res.
4. Return res.
5. The time complexity is O(n), where n is the number of nodes in the tree, since we visit each node once. The space complexity is O(n) as well, due to the storage of the result and the queue. """    