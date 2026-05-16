#347. Top K Frequent Elements
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
                
#example 1:
nums = [1,1,1,2,2,3]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k)) # Output: [1,2]

#example 2:
nums = [1]
k = 1
solution = Solution()
print(solution.topKFrequent(nums, k)) # Output: [1] 

#example 3:
nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k)) # Output: [1,2]

"""walkthrough:
1. We create a dictionary `count` to count the frequency of each number in the input list `nums`.
2. We create a list of lists `freq` where the index represents the frequency and the value at that index is a list of numbers that have that frequency.
3. We iterate through the `count` dictionary and populate the `freq` list based on the frequency of each number.
4. We initialize an empty list `res` to store the result.
5. We iterate through the `freq` list in reverse order (starting from the highest frequency) and append numbers to the `res` list until we have collected `k` numbers.
6. Finally, we return the `res` list containing the top `k` frequent elements.
This approach has a time complexity of O(n) for counting frequencies and O(n) for building the `freq` list, resulting in an overall time complexity of O(n). The space complexity is also O(n) due to the `count` dictionary and the `freq` list."""