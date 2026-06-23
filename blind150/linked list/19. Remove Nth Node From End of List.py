#19. Remove Nth Node From End of List
"""Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?"""

#answer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
    
#example 1:
"""Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]"""
#example 2:
"""Input: head = [1], n = 1     
Output: []"""   
#example 3:
"""Input: head = [1,2], n = 1   
Output: [1]"""  


"""walkthrough:
1. Create a dummy node that points to the head of the list. This helps handle edge cases, such as when the head needs to be removed.
2. Initialize two pointers, left and right. Set left to the dummy node and right to the head of the list.
3. Move the right pointer n steps ahead in the list. This creates a gap of n nodes between the left and right pointers.
4. Move both pointers (left and right) one step at a time until the right pointer reaches the end of the list. At this point, the left pointer will be just before the node that needs to be removed.
5. Remove the nth node from the end by changing the next pointer of the left node to skip the node to be removed (i.e., left.next = left.next.next).
6. Return the next node of the dummy node, which is the new head of the modified list. This handles cases where the head of the list was removed.       
"""