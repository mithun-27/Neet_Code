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

#example usage
# Create a linked list: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
sol = Solution()
sol.reorderList(head)
# Print the reordered list: 1 -> 4 -> 2 -> 3
current = head
while current:
    print(current.val, end=' ')
    current = current.next
# Output: 1 4 2 3
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)
sol.reorderList(head2)
# Print the reordered list: 1 -> 5 -> 2 -> 4 ->
current = head2
while current:
    print(current.val, end=' ')
    current = current.next
# Output: 1 5 2 4 3

"""walktghrough the code:
1. We start by finding the middle of the linked list using the slow and fast pointer technique. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. When the fast pointer reaches the end of the list, the slow pointer will be at the middle.
2. We then reverse the second half of the linked list starting from the node after the slow pointer. We use a standard linked list reversal technique where we keep track of the previous node and the current node, and we reverse the links between them.
3. Finally, we merge the two halves of the linked list. We take one node from the first half and one node from the reversed second half, and we link them together. We continue this process until we have merged all nodes from the second half into the first half.
4. The function does not return anything as it modifies the linked list in place.
This approach has a time complexity of O(n) and a space complexity of O(1) since we are only using a constant amount of extra space for the pointers.
"""