#435. Non-overlapping Intervals
"""Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104"""

#answer
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[1])
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                res += 1
            else:
                prevEnd = intervals[i][1]


        return res
    
#example
intervals = [[1,2],[2,3],[3,4],[1,3]]
s = Solution()
print(s.eraseOverlapIntervals(intervals))

"""walkthrough:
1. Sort the intervals based on their end time. This allows us to always consider the interval that finishes earliest, which helps in minimizing the number of intervals we need to remove.
2. Initialize a variable prevEnd to keep track of the end time of the last non-overlapping interval we added to our count. Start with the end time of the first interval.
3. Iterate through the sorted intervals starting from the second interval. For each interval, check if its start time is less than the prevEnd. If it is, it means this interval overlaps with the previous one, and we need to remove it, so we increment our result counter. If it does not overlap, we update prevEnd to the end time of the current interval.
4. Finally, return the count of removed intervals.
This approach ensures that we are always keeping the interval that ends earliest, which allows us to maximize the number of non-overlapping intervals and minimize the number of removals."""