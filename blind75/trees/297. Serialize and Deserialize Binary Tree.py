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
    
#example usage
# Create a binary tree:
# Tree:        1
#             /  \
#            2    3
#                /  \
#               4    5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
codec = Codec()
serialized = codec.serialize(root)
print("Serialized:", serialized)
deserialized_root = codec.deserialize(serialized)
print("Deserialized Root Value:", deserialized_root.val)  # Output: 1
print("Deserialized Left Child Value:", deserialized_root.left.val)  # Output: 2
print("Deserialized Right Child Value:", deserialized_root.right.val)  # Output: 3
print("Deserialized Right Left Child Value:", deserialized_root.right.left.val)  # Output: 4
print("Deserialized Right Right Child Value:", deserialized_root.right.right.val)  # Output: 5


"""walkthrough
1. **Serialization**:
   - We use a breadth-first traversal (level order) to serialize the tree.
   - We initialize a queue with the root node and an empty list `res` to store the serialized values.
   - For each node, if it is not null, we append its value to `res` and enqueue its left and right children. If it is null, we append "N" to represent a null node.
   - Finally, we join the list `res` into a string with commas as separators.   
2. **Deserialization**:
   - We split the input string by commas to get a list of values.
   - If the first value is "N", it means the tree is empty, and we return None.
   - We create the root node using the first value and initialize a queue with the root node.
   - We use an index to keep track of our position in the list of values. For each node dequeued, we check the next two values in the list to determine if they represent left and right children. If they are not "N", we create new nodes and enqueue them.
   - We continue this process until we have processed all values in the list, resulting in the reconstructed binary tree.   
3. **Complexity**:
   - The time complexity for both serialization and deserialization is O(n), where n is the number of nodes in the tree, since we need to visit each node once.
   - The space complexity is also O(n) for both operations, as we may need to store all nodes in the queue and the resulting string.
This approach ensures that we can accurately serialize and deserialize any binary tree structure, including those with null nodes, while maintaining a clear and efficient algorithm.   
"""