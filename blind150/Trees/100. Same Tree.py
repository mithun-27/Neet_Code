#100. Same Tree
"""Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104"""

#answer 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from sqlalchemy import true


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                nodeP = q1.popleft()
                nodeQ = q2.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                q1.append(nodeP.left)
                q1.append(nodeP.right)
                q2.append(nodeQ.left)
                q2.append(nodeQ.right)

        return True
    
#example 1:     
"""input: p = [1,2,3], q = [1,2,3]
output: true"""
#example 2:
"""input: p = [1,2], q = [1,null,2] ]
output: false"""
#example 3:
"""input: p = [1,2,1], q = [1,1,2]
output: false"""

"""walkthrough:
1. Create two queues, q1 and q2, to hold the nodes of the two trees.
2. While both queues are not empty, do the following:
   a. For each node in the current level of the trees, dequeue a node from each queue.
   b. If both nodes are None, continue to the next iteration.
   c. If one node is None or the values of the nodes are not equal, return False.
   d. Enqueue the left and right children of both nodes into their respective queues.
3. If the loop completes without returning False, return True, indicating that the trees are the same.  
4. The time complexity of this solution is O(n), where n is the number of nodes in the trees, since we visit each node once. The space complexity is also O(n) in the worst case, due to the storage of nodes in the queues."""