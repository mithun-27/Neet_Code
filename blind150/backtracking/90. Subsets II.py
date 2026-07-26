#90. Subsets II
"""Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10"""

#answer
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        prev_Idx = idx = 0

        for i in range(len(nums)):
            idx = prev_idx if i >= 1 and nums[i] == nums[i - 1] else 0
            prev_idx = len(res)
            for j in range(idx, prev_idx):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)

        return res

#example
"""Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 """

"""Walkthrough:
1. We want to generate all possible subsets of the given array `nums`, but the array may contain duplicate elements, so the final result must not contain duplicate subsets.
2. We first sort the `nums` array so that duplicate elements are placed next to each other. This makes it easier to identify and handle duplicates.
3. We initialize the result list with the empty subset (`[[]]`), since every set always contains the empty subset.
4. We iterate through each element in the sorted array. For each element, we determine the range of existing subsets that should be extended.
5. If the current element is different from the previous element, we extend every existing subset in the result list by adding the current element.
6. If the current element is the same as the previous element, we extend only the subsets that were added during the previous iteration. This prevents generating duplicate subsets.
7. For each selected subset, we create a copy, append the current element, and add the new subset to the result list.
8. We repeat this process until every element has been processed. Since duplicate elements only extend the newly created subsets from the previous step, every subset is generated exactly once.
9. The final result contains all unique subsets of the input array. The time complexity is `O(n × 2^n)` in the worst case because up to `2^n` subsets are generated, and copying each subset takes up to `O(n)` time. The auxiliary space complexity is `O(n)` for temporary subset creation (excluding the output), while the total space including the returned subsets is `O(n × 2^n)`."""