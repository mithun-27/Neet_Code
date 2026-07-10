#98. Validate Binary Search Tree
"""Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1"""

#example 1:
"""Input: root = [2,1,3]
Output: true"""
#example 2:
"""Input: root = [5,1,4,null,null,3,6]  
Output: false"""


"""walkthrough:
1. To validate a binary search tree (BST), we can use a recursive approach that checks whether each node's value falls within a valid range defined by its ancestors.
2. We can define a helper function that takes a node and two parameters, min_val and max_val, representing the valid range for the node's value. Initially, we can set min_val to negative infinity and max_val to positive infinity.
3. For each node, we check if its value is within the range (min_val, max_val). If it is not, we return false. If it is valid, we recursively check the left and right subtrees, updating the valid range accordingly. For the left child, we update max_val to the current node's value, and for the right child, we update min_val to the current node's value.
4. If we reach a null node, we return true, as an empty subtree is considered valid. Finally, we return the result of the helper function for the root node.
5. The time complexity of this approach is O(n), where n is the number of nodes in the binary tree, as we visit each node once. The space complexity is O(h), where h is the height of the tree, due to the recursive call stack. In the worst case, for a skewed tree, the space complexity can be O(n), but for a balanced tree, it will be O(log n).
"""