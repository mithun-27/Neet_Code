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
 """

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
    
#example usage
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
sol = Solution()
new_head = sol.removeNthFromEnd(head, 2)
# Print the modified list: 1 -> 2 -> 3 -> 5
current = new_head
while current:
    print(current.val)
    current = current.next
#19. Remove Nth Node From End of List

"""walkthrough
1. We create a dummy node that points to the head of the list. This helps us handle edge cases, such as when we need to remove the head node.
2. We initialize two pointers, left and right. The left pointer starts at the dummy node, and the right pointer starts at the head of the list.
3. We move the right pointer n steps ahead in the list. This creates a gap of n nodes between the left and right pointers.
4. We then move both pointers (left and right) one step at a time until the right pointer reaches the end of the list. At this point, the left pointer will be just before the node we want to remove.
5. We update the next pointer of the left node to skip the node we want to remove, effectively removing it from the list.
6. Finally, we return the next node of the dummy node, which is the new head of the modified list. This handles cases where the head node was removed."""