#56. Merge Intervals
"""Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104"""

#answer
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)

        mp = [0] * (max_val + 1)
        for start, end in intervals:
            mp[start] = max(end + 1, mp[start])

        res = []
        have = -1
        interval_start = -1
        for i in range(len(mp)):
            if mp[i] != 0:
                if interval_start == -1:
                    interval_start = i
                have = max(mp[i] - 1, have)
            if have == i:
                res.append([interval_start, have])
                have = -1
                interval_start = -1

        if interval_start != -1:
            res.append([interval_start, have])

        return res
    
#example
intervals = [[1,3],[2,6],[8,10],[15,18]]
s = Solution()
print(s.merge(intervals))


"""walkthrough:
1. We first find the maximum starting point among all intervals to determine the size of a mapping array mp that will help us track the end points of intervals.        
2. We initialize an array mp of size max_val + 1 with all elements set to 0. We then iterate through each interval and update mp at the index corresponding to the start of the interval to be the maximum of the current value at that index and the end of the interval plus one (to account for zero-based indexing).        
3. We initialize an empty list res to store the resulting merged intervals, and two variables have and interval_start to keep track of the current interval we are merging. We iterate through the mp array, and for each index:
   a. If mp[i] is not zero, it means there is an interval starting at index i. If interval_start is -1, we set it to i to mark the start of a new interval. We also update have to be the maximum of its current value and mp[i] - 1 (to get the actual end point of the interval).
   b. If have is equal to i, it means we have reached the end of the current interval we are merging. We append the interval [interval_start, have] to res, and reset have and interval_start to -1 to prepare for the next interval.       
4. After the loop, if interval_start is not -1, it means there is an interval that has not been added to res yet, so we append it as well. Finally, we return the resulting list of merged intervals.       
This approach effectively uses a mapping array to track the intervals and merge them in a single pass, resulting in an efficient solution to the problem.       
"""