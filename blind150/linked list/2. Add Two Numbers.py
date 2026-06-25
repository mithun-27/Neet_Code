#2. Add Two Numbers
"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros."""

#answer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
#example:1
"""Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]"""
#example:2
"""Input: l1 = [0], l2 = [0]
Output: [0]"""
#example:3
"""Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]"""    

"""WALKTHROUGH
1. Create a dummy node to serve as the head of the result linked list.
2. Initialize a pointer (cur) to the dummy node and a variable (carry) to 0 to keep track of any carry-over during addition.
3. Iterate through the linked lists l1 and l2 until both are fully traversed and there is no carry left:
   a. Retrieve the values of the current nodes of l1 and l2 (v1 and v2). If a list is exhausted, use 0 as the value.
   b. Calculate the sum of v1, v2, and carry. Update carry for the next iteration and determine the new digit to be added to the result linked list.
   c. Create a new node with the calculated digit and link it to the result linked list.
   d. Move the cur pointer to the newly created node and advance l1 and l2 pointers to their next nodes if they exist.
4. After the loop, return the next node of the dummy, which is the head of the resulting linked list representing the sum of the two numbers.       
5. The time complexity of this solution is O(max(m, n)), where m and n are the lengths of the two linked lists. The space complexity is O(max(m, n)) for the new linked list created to store the result."""
