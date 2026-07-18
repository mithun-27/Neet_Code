#215. Kth Largest Element in an Array
"""Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104"""

#answer
from typing import List


class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        mid = (left + right) >> 1
        nums[mid], nums[left + 1] = nums[left + 1], nums[mid]

        if nums[left] < nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left + 1] < nums[right]:
            nums[left + 1], nums[right] = nums[right], nums[left + 1]
        if nums[left] < nums[left + 1]:
            nums[left], nums[left + 1] = nums[left + 1], nums[left]

        pivot = nums[left + 1]
        i = left + 1
        j = right

        while True:
            while True:
                i += 1
                if not nums[i] > pivot:
                    break
            while True:
                j -= 1
                if not nums[j] < pivot:
                    break
            if i > j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        nums[left + 1], nums[j] = nums[j], nums[left + 1]
        return j

    def quickSelect(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1

        while True:
            if right <= left + 1:
                if right == left + 1 and nums[right] > nums[left]:
                    nums[left], nums[right] = nums[right], nums[left]
                return nums[k]

            j = self.partition(nums, left, right)

            if j >= k:
                right = j - 1
            if j <= k:
                left = j + 1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, k - 1)
    
#example 1:
solution = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(solution.findKthLargest(nums, k)) #Output: 5
#example 2:
nums = [3,2,3,1,2,4,5,5,6]
k = 4   
print(solution.findKthLargest(nums, k)) #Output: 4
#example 3:
nums = [7,10,4,3,20,15]
k = 3
print(solution.findKthLargest(nums, k)) #Output: 10


"""walkthrough:
1. The function `findKthLargest` takes an array of integers `nums` and an integer `k`, and returns the kth largest element in the array.
2. The function uses the Quickselect algorithm, which is a selection algorithm to find the kth smallest/largest element in an unordered list. It is related to the quicksort sorting algorithm.
3. The `quickSelect` function is called with the input array and k-1 (since the array is 0-indexed). It initializes two pointers, `left` and `right`, to the start and end of the array, respectively.
4. The `partition` function is used to rearrange the elements in the array such that all elements greater than the pivot are on the left side and all elements less than the pivot are on the right side. The pivot is chosen as the median of three elements (the first, middle, and last elements) to improve performance.
5. The `quickSelect` function continues to partition the array until the pivot index matches k-1. If the pivot index is greater than k-1, it narrows the search to the left side of the array; if it is less than k-1, it narrows the search to the right side.
6. Once the pivot index matches k-1, the function returns the element at that index, which is the kth largest element in the original array.        
"""