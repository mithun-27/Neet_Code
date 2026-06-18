#206. Reverse Linked List
"""Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000"""

#answer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
#example 1:
"""Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]"""
#example 2:
"""Input: head = [1,2]
Output: [2,1]"""
#example 3:
"""Input: head = []
Output: []"""

"""walkthrough:
1. We initialize two pointers, `prev` and `curr`. `prev` starts as `None` and `curr` starts at the head of the list.
2. We iterate through the list until `curr` is `None`. In each iteration, we store the next node in a temporary variable `temp`, reverse the link by pointing `curr.next` to `prev`, then move `prev` and `curr` one step forward.
3. Finally, we return `prev`, which will be the new head of the reversed list.      
Time complexity: O(n) where n is the number of nodes in the linked list, since we need to traverse the entire list once.
Space complexity: O(1) since we are using only a constant amount of extra space for the pointers.   
"""