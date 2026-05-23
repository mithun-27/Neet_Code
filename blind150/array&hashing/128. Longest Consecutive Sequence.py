#128. Longest Consecutive Sequence
"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109"""

#answer
from git import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
"""walkthrough:
1. We create a set of the input numbers for O(1) lookups.
2. We iterate through each number in the set. For each number, we check if it is the start of a sequence (i.e., if num - 1 is not in the set).
3. If it is the start of a sequence, we initialize a length counter and keep checking for the next consecutive numbers (num + length) in the set, incrementing the length counter until we no longer find consecutive numbers.
4. We keep track of the longest sequence length found and return it at the end.
This algorithm runs in O(n) time because each number is processed at most twice (once when checking if it's the start of a sequence and once when counting the length of the sequence). """    