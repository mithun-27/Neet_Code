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
    
#example usage
# Create a linked list 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
sol = Solution()
reversed_head = sol.reverseList(head)
# Print the reversed linked list
current = reversed_head
while current:
    print(current.val)  # Output: 5, 4, 3, 2, 1
    current = current.next

    
"""walkthrough:
1. We initialize two pointers, prev and curr, to keep track of the previous and current nodes in the linked list. Initially, prev is set to None and curr is set to the head of the list.
2. We enter a while loop that continues until curr is None, which means we have reached the end of the list.
3. Inside the loop, we store the next node of curr in a temporary variable temp. This is necessary because we will be changing the next pointer of curr, and we don't want to lose the reference to the rest of the list.
4. We then reverse the next pointer of curr by setting curr.next to prev. This effectively reverses the link between curr and prev.
5. We move the prev pointer to curr, and the curr pointer to temp, which is the next node in the original list.
6. After the loop, prev will be pointing to the new head of the reversed list, so we return prev.
"""