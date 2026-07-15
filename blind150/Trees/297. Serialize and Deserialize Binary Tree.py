#297. Serialize and Deserialize Binary Tree
"""Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index += 1
            if vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index += 1
        return root
    
#example 1:
"""Input: root = [1,2,3,null,null,4,5]      
Output: [1,2,3,null,null,4,5]"""
#example 2:
"""Input: root = []
Output: []"""
#example 3:
"""Input: root = [1]
Output: [1]"""

"""walkthrough:
1. Serialize:
- If the root is None, return "N".
- Otherwise, use a queue to perform a level-order traversal and append each node's value or "N" for null nodes.
2. Deserialize:
- Split the serialized string by commas.
- If the first value is "N", return None.
- Otherwise, create the root node and use a queue to reconstruct the tree level by level.   
3. Return the reconstructed tree's root node.
4. The serialized string can be used to reconstruct the original tree structure accurately.
5. The algorithm handles edge cases such as empty trees and single-node trees effectively.
6. The time complexity for both serialization and deserialization is O(n), where n is the number of nodes in the tree, as each node is processed once. The space complexity is also O(n) due to the storage of the serialized string and the queue used for traversal.  
""" 
