#23. Merge k Sorted Lists
"""You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104."""

#answer
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next
    
#example usage
# Create linked lists: 1->4->5, 1->3->4, 2->6
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
list3 = ListNode(2)
list3.next = ListNode(6)
lists = [list1, list2, list3]
sol = Solution()
merged_head = sol.mergeKLists(lists)
# Print the merged linked list: 1->1->2->3->4->4->5->6
current = merged_head
while current:
    print(current.val, end=' ')
    current = current.next

"""walkthrough:
1. We define a function mergeKLists that takes a list of linked lists as input.
2. We check if the input list is empty or contains only empty lists. If so, we return None.
3. We use a while loop to continue merging until there is only one linked list left in the lists.
4. Inside the while loop, we create an empty list mergedLists to store the merged linked lists.
5. We iterate through the lists in pairs (i and i + 1) and merge them using the mergeList function.
6. The mergeList function takes two linked lists as input and merges them into a single sorted linked list.
7. We create a dummy node to help with merging and a tail pointer to keep track of the end of the merged list.
8. We compare the values of the current nodes of both lists and append the smaller one to the merged list, moving the corresponding pointer forward.
9. After the while loop, we check if there are any remaining nodes in either list and append them to the merged list.
10. Finally, we return the head of the merged linked list, which is dummy.next.
11. We also provide an example usage of the mergeKLists function, where we create three linked lists, merge them, and print the merged linked list.
"""