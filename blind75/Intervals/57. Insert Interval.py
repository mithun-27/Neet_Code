#57. Insert Interval
"""You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105"""

#answer
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res
    
#example
intervals = [[1,3],[6,9]]
newInterval = [2,5]
s = Solution()
print(s.insert(intervals, newInterval))

"""walkthrough:
1. We initialize an empty list res to store the resulting intervals after insertion and merging.        
2. We iterate through each interval in the input intervals list using a for loop. For each interval, we check three conditions:
   a. If the end of the newInterval is less than the start of the current interval, it means there is no overlap and we can safely add newInterval to res and return the combined list of res and the remaining intervals.
   b. If the start of the newInterval is greater than the end of the current interval, it means there is no overlap and we can safely add the current interval to res.
   c. If neither of the above conditions are met, it means there is an overlap between newInterval and the current interval. In this case, we merge them by updating newInterval to be a new interval that starts at the minimum of the two starting points and ends at the maximum of the two ending points.   
3. After the loop, if newInterval has not been added to res (which means it overlaps with the last interval), we append it to res.
4. Finally, we return the resulting list res, which contains the merged intervals after inserting newInterval.
The time complexity of this solution is O(n), where n is the number of intervals in the input list. This is because we iterate through the intervals once to check for overlaps and merge them if necessary. The space complexity is also O(n) in the worst case, if all intervals overlap and we need to create a new list to store the merged intervals."""