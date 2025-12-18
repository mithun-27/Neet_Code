# 347. Top K Frequent Elements
"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique."""

#answer
from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
#example usage
solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))  # Output: [1,2]
print(solution.topKFrequent([1], 1))  # Output: [1]
print(solution.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))  # Output: [1,2]

"""WALKTHROUGH
1. We import Counter from the collections module and List from the typing module.
2. We define a class Solution with a method topKFrequent that takes a list of integers nums and an integer k as input.
3. We initialize an empty dictionary count to store the frequency of each number in nums.
4. We create a list freq of empty lists, where the index represents the frequency of numbers. The length of freq is len(nums) + 1 to accommodate frequencies from 0 to len(nums).
5. We iterate through each number in nums and update its count in the count dictionary.
6. We then iterate through the count dictionary and append each number to the corresponding index in the freq list based on its frequency.
7. We initialize an empty list res to store the result.
8. We iterate through the freq list in reverse order (from highest frequency to lowest).
9. For each frequency, we iterate through the numbers in freq[i] and append them to res.
10. If the length of res reaches k, we return res as the final result.
"""