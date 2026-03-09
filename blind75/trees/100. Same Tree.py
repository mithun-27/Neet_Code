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
-104 <= Node.val <= 104
"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
    
#example usage
# Create two binary trees:
# Tree 1:        1
#               / \
#              2   3
# Tree 2:        1
#               / \
#              2   3
# Check if the two trees are the same
# The output will be true, as both trees are structurally identical and have the same node values.
# Create two binary trees:
# Tree 1:        1
#               /
#              2
# Tree 2:        1
#                 \
#                  2
# Check if the two trees are the same
# The output will be false, as the trees are not structurally identical (one has a left child while the other has a right child).
# Create two binary trees:
# Tree 1:        1
#               / \
#              2   1
# Tree 2:        1  
#               / \
#              1   2
# Check if the two trees are the same
# The output will be false, as the trees are structurally identical but have different node values (the left child of the root in Tree 1 has a value of 2, while in Tree 2 it has a value of 1).    

"""walkthrough
1. Initialize two queues, q1 and q2, to perform a level-order traversal of both trees simultaneously. Start by adding the root nodes of both trees to their respective queues.
2. While both queues are not empty, perform the following steps:
   a. For each node in the current level of q1, pop the node from q1 and the corresponding node from q2.
   b. If both nodes are None, continue to the next iteration (they are considered the same).
   c. If one of the nodes is None or their values are not equal, return False (the trees are not the same).
   d. If the nodes are valid and have the same value, add their left and right children to their respective queues for further comparison.          
3. If the loop completes without finding any differences, return True (the trees are the same).
This algorithm effectively compares the two trees level by level, ensuring that both the structure and the values of the nodes are identical. The time complexity is O(n), where n is the number of nodes in the smaller tree, as we may need to compare all nodes in the worst case. The space complexity is also O(n) due to the queues used for traversal.   
"""