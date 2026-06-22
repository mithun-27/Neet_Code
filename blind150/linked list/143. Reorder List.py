#143. Reorder List
"""You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000"""

#answer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

#example 1:
"""Input: head = [1,2,3,4]
Output: [1,4,2,3]"""
#example 2:
"""Input: head = [1,2,3,4,5]    
Output: [1,5,2,4,3]"""  
#example 3:
"""Input: head = [1]            
Output: [1]"""  

"""walkthrough:
1. Use the slow and fast pointer technique to find the middle of the linked list.                                       
2. Reverse the second half of the linked list.
3. Merge the two halves of the linked list together in the required order.          
4. The first half of the list remains in its original order, while the second half is reversed and interleaved with the first half. This results in the desired reordered list format.      
5. The algorithm runs in O(n) time complexity, where n is the number of nodes in the linked list, and uses O(1) additional space since we are modifying the list in place.  
"""