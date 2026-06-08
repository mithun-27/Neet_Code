#739. Daily Temperatures
"""Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100"""

#answer
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]

            if j < n:
                res[i] = j - i
        return res
    
#example 1:
#Input: temperatures = [73,74,75,71,69,72,76,73]
#Output: [1,1,4,2,1,1,0,0]
#example 2:
#Input: temperatures = [30,40,50,60]
#Output: [1,1,1,0]  
#example 3: 
#Input: temperatures = [30,60,90]   
#Output: [1,1,0]    


"""walkthrough :
1. We initialize an array res of the same length as temperatures with all values set to 0. This array will store the number of days until a warmer temperature for each day.
2. We iterate through the temperatures array in reverse order, starting from the second to last element down to the first element.          
3. For each day i, we initialize a variable j to i + 1, which represents the next day.          
4. We enter a while loop that continues as long as j is within the bounds of the temperatures array and the temperature at day j is less than or equal to the temperature at day i. Inside the loop:
   - If res[j] is 0, it means there are no warmer days ahead for day j, so we set j to n (the length of the temperatures array) to exit the loop.
   - Otherwise, we update j by adding res[j] to it, which allows us to skip over days that we already know are not warmer than day i.   
5. After the while loop, if j is still within the bounds of the temperatures array, it means we found a warmer day for day i. We calculate the number of days until that warmer day by subtracting i from j and store it in res[i].
6. Finally, we return the res array, which contains the number of days until a warmer temperature for each day.
This approach efficiently computes the result by leveraging previously computed results to skip unnecessary comparisons, resulting in a time complexity of O(n) and a space complexity of O(n). """