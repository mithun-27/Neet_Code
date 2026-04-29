#252. Meeting Rooms
"""Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000"""

#answer
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda pair: pair[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True
    
#example
intervals = [(0,30),(5,10),(15,20)]
s = Solution()
print(s.canAttendMeetings(intervals))

"""walkthrough:
1. Sort the intervals based on their start time. This allows us to check for overlapping meetings in a sequential manner.
2. Iterate through the sorted intervals starting from the second interval. For each interval, compare its start time with the end time of the previous interval. If the start time of the current interval is less than the end time of the previous interval, it means there is a conflict, and we can return False immediately.   
3. If we finish iterating through all intervals without finding any conflicts, we can return True, indicating that a person can attend all meetings without any overlaps.
This approach ensures that we are checking for overlaps in a straightforward manner, and the sorting step helps us to efficiently identify any conflicts between meetings. The time complexity of this solution is O(n log n) due to the sorting step, and the space complexity is O(1) if we ignore the space used for sorting.""" 
