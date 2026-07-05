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
    
#example 1:
"""input: root = [3,4,5,1,2], subRoot = [4,1,2] 
output: true"""
#example 2:
"""input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
output: false"""
#example 3:
"""input: root = [1,1], subRoot = [1]   
output: true"""

"""walkthrough:
1. Serialize both trees using pre-order traversal, marking null nodes with a special character (e.g., "$").
2. Concatenate the serialized subRoot with a separator (e.g., "|") and the serialized root.
3. Use the Z-function algorithm to find occurrences of the serialized subRoot in the serialized root.   
4. If any Z-value equals the length of the serialized subRoot, return True (indicating subRoot is a subtree of root). Otherwise, return False.
5. The Z-function efficiently computes the longest substring matches, allowing us to check for subtree presence in linear time relative to the combined length of the serialized strings.
6. This approach ensures that we can handle the constraints of the problem efficiently, even for larger trees.  
7. The overall time complexity is O(n + m), where n is the number of nodes in root and m is the number of nodes in subRoot, due to the serialization and Z-function processing. 
8. The space complexity is also O(n + m) for storing the serialized strings and Z-values.   
9. This method is efficient and avoids the need for repeated tree comparisons, making it suitable for larger inputs within the given constraints.   
10. The use of serialization and string matching techniques provides a clear and effective solution to the subtree problem, leveraging well-known algorithms for string processing. 
11. The serialization step ensures that the structure and values of the trees are captured in a linear format, allowing for straightforward comparison. 
12. The Z-function is a powerful tool for pattern matching, enabling us to efficiently find occurrences of the serialized subRoot within the serialized root without the need for nested loops or repeated comparisons.
13. Overall, this approach combines tree serialization with advanced string matching techniques to provide a robust solution to the subtree problem, ensuring correctness and efficiency within the specified constraints.
14. The solution is designed to handle edge cases, such as when either tree is empty, by appropriately marking null nodes during serialization. This ensures that the comparison accurately reflects the structure of the trees, even in cases where one tree may have missing children.    
15. The use of a special character to denote null nodes during serialization is crucial for maintaining the integrity of the tree structure in the serialized string, allowing for accurate subtree detection.  
16. The overall design of the solution emphasizes clarity and efficiency, making it suitable for a wide range of binary tree configurations while adhering to the problem's constraints.    
17. The solution is implemented in Python, leveraging the language's capabilities for handling data structures and algorithms effectively. The use of classes and methods provides a clear organization of the code, facilitating understanding and maintenance.    
18. The implementation is designed to be easily understandable, with clear method names and logical flow, making it accessible to developers with varying levels of experience in tree algorithms and string processing techniques. 
"""  
