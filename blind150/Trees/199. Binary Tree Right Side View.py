#199. Binary Tree Right Side View
"""Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100"""

#answer

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
    
#example 1
""" Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4] """
#example 2
""" Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5] """
#example 3
""" Input: root = [1,null,3]    
Output: [1,3] """
#example 4
""" Input: root = []
Output: [] """

"""walkthrough:
1. Initialize an empty list res to store the right side view of the binary tree.
2. Initialize a queue (deque) and add the root node to it.
3. While the queue is not empty, do the following:
   a. Initialize a variable rightSide to None. This will hold the rightmost node at the current level.
   b. Get the number of nodes at the current level (qLen).
   c. For each node at the current level, do the following:
      i. Pop a node from the queue.
      ii. If the node is not None, update rightSide to this node and add its left and right children to the queue.
   d. After processing all nodes at the current level, if rightSide is not None, append its value to res.
4. Return res, which contains the values of the nodes visible from the right side of the binary tree.
5. The time complexity of this solution is O(n), where n is the number of nodes in the binary tree, as we visit each node exactly once. The space complexity is also O(n) in the worst case, which occurs when the binary tree is completely unbalanced (e.g., a linked list). In the best case, when the tree is balanced, the space complexity would be O(log n) due to the height of the tree.   
"""