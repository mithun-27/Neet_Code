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
    
#example:1
"""Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]"""
#example:2
"""Input: lists = []
Output: []"""

"""walkthrough:
1. Check if the input list of linked lists is empty or has no elements. If so, return None.
2. While there is more than one linked list in the input, perform the following steps:              
   a. Initialize an empty list called mergedLists to store the merged linked lists.
   b. Iterate through the input lists in pairs (two at a time) using a for loop with a step of 2.
   c. For each pair of linked lists (l1 and l2), call the mergeList function to merge them into a single sorted linked list.
   d. Append the merged linked list to the mergedLists list.    
   e. If there is an odd number of linked lists, the last linked list will be merged with None, effectively keeping it unchanged.
3. After merging all pairs of linked lists, update the input lists to be the mergedLists.
4. Repeat the process until there is only one linked list left in the input lists.
5. Return the final merged linked list, which is the only element left in the input lists.          
6. The mergeList function takes two sorted linked lists (l1 and l2) as input and merges them into a single sorted linked list. It uses a dummy node to simplify the merging process and a tail pointer to keep track of the last node in the merged list.
7. The time complexity of this solution is O(N log k), where N is the total number of nodes across all linked lists and k is the number of linked lists. The space complexity is O(1) since we are merging the lists in place without using any additional data structures.     
"""