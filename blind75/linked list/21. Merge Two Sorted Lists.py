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

#example usage
# Create first linked list 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)                       
# Create second linked list 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
sol = Solution()
merged_head = sol.mergeTwoLists(list1, list2)
# Print the merged linked list
current = merged_head
while current:
    print(current.val)  # Output: 1, 1, 2, 3, 4, 4
    current = current.next


"""walkthrough: 
1. We create a dummy node to serve as the starting point of the merged linked list. We also create a pointer node that will be used to build the merged list.   
2. We enter a loop that continues until either list1 or list2 is exhausted. Inside the loop, we compare the values of the current nodes of list1 and list2. We append the smaller value to the merged list and move the corresponding pointer (list1 or list2) to the next node. We also move the node pointer to the next position in the merged list. 
3. After the loop, one of the lists may still have remaining nodes. We append the remaining nodes to the merged list by setting node.next to the non-empty list (list1 or list2).   
4. Finally, we return dummy.next, which is the head of the merged linked list, since dummy is a placeholder node.
5. The time complexity of this algorithm is O(n + m), where n and m are the lengths of list1 and list2, respectively, because we traverse both lists once. The space complexity is O(1) since we are only using a few pointers to build the merged list without any additional data structures."""  

