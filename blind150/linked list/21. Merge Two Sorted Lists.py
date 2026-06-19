#21. Merge Two Sorted Lists
"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order."""

#answer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next

#example 1:
"""Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]"""
#example 2:
"""Input: list1 = [], list2 = []
Output: []"""
#example 3:
"""Input: list1 = [], list2 = [0]
Output: [0]"""

"""walkthrough:
1. We create a dummy node to serve as the starting point of the merged list and a pointer `node` that will be used to build the merged list.    
2. We iterate through both lists while both `list1` and `list2` are not empty. In each iteration, we compare the values of the current nodes of both lists. We attach the smaller node to the merged list and move the pointer of that list forward. We also move the `node` pointer forward to continue building the merged list.  
3. After the loop, one of the lists may still have remaining nodes. We attach the remaining nodes to the merged list by setting `node.next` to the non-empty list (either `list1` or `list2`).  
4. Finally, we return `dummy.next`, which points to the head of the merged list.
Time complexity: O(n + m) where n and m are the lengths of list1 and list2, respectively, since we traverse both lists once.
Space complexity: O(1) since we are using only a constant amount of extra space for the pointers.   
"""