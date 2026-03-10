#572. Subtree of Another Tree

"""Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104"""

#answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from numpy import array


class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "$#"

        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))

    def z_function(self, s: str) -> list:
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = self.serialize(root)
        serialized_subRoot = self.serialize(subRoot)
        combined = serialized_subRoot + "|" + serialized_root

        z_values = self.z_function(combined)
        sub_len = len(serialized_subRoot)

        for i in range(sub_len + 1, len(combined)):
            if z_values[i] == sub_len:
                return True
        return False
    
#example usage
# Create two binary trees:
# Tree 1:        3
#               / \
# Tree 2:        4
#               / \
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)
# Check if subRoot is a subtree of root
# The output will be true, as subRoot is a subtree of root with the same structure and node values.


"""walkthrough the code
1. The `serialize` function converts a binary tree into a string representation. It uses preorder traversal to create a unique string for each tree structure and node values. The special marker "$#" is used to denote null nodes, ensuring that different tree structures produce different strings.
2. The `z_function` computes the Z-array for a given string, which is used to find occurrences of the pattern (subRoot) in the text (root). The Z-array stores the length of the longest substring starting from each position that matches a prefix of the string.
3. The `isSubtree` function first serializes both the root and subRoot trees. It then combines the serialized subRoot and root strings with a separator (|) to create a single string for pattern matching.
4. The Z-function is applied to the combined string, and the function checks if any position in the Z-array matches the length of the serialized subRoot. If a match is found, it means that subRoot is a subtree of root, and the function returns true. If no match is found after checking all positions, it returns false.
This approach efficiently checks for the presence of subRoot in root by leveraging string matching techniques, resulting in a time complexity of O(n + m), where n is the length of the serialized root and m is the length of the serialized subRoot.  
"""