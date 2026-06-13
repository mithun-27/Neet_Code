#875. Koko Eating Bananas
""""Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""

#answer
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
    
#example 1:
"""Input: piles = [3,6,7,11], h = 8 
Output: 4  """
#example 2:
"""Input: piles = [30,11,23,4,20], h = 5
Output: 30  """     
#example 3:
"""Input: piles = [30,11,23,4,20], h = 6
Output: 23  """ 

"""walkthrough: 
1. We start by initializing two pointers, l and r, to represent the minimum and maximum possible eating speeds. The minimum speed is 1 (the slowest Koko can eat), and the maximum speed is the largest pile of bananas (the fastest Koko would need to eat to finish in one hour).         
2. We also initialize a variable res to store the minimum eating speed that allows Koko to finish eating all the bananas within h hours. Initially, we set res to r, which is the maximum possible speed.       
3. We enter a while loop that continues as long as l is less than or equal to r. This loop will help us narrow down our search for the minimum eating speed.        
4. Inside the loop, we calculate the middle eating speed k using the formula (l + r) // 2. This gives us a candidate eating speed to test.          
5. We then calculate the total time it would take for Koko to eat all the bananas at speed k. We iterate through each pile of bananas and use math.ceil(float(p) / k) to determine how many hours it would take to eat that pile at speed k. We sum up the total time for all piles.    
6. If the total time is less than or equal to h, it means Koko can finish eating all the bananas at speed k. In this case, we update res to k (since we want the minimum speed) and move the right pointer r to k - 1 to search for a potentially slower speed. If the total time is greater than h, it means Koko cannot finish eating all the bananas at speed k, so we move the left pointer l to k + 1 to search for a faster speed.        
7. Once the while loop ends, res will contain the minimum eating speed that allows Koko to finish eating all the bananas within h hours, and we return res. 
8. The time complexity of this solution is O(n log m), where n is the number of piles and m is the maximum number of bananas in a pile. This is because we perform a binary search on the range of possible eating speeds (log m) and for each candidate speed, we calculate the total time to eat all the bananas (O(n)). The space complexity is O(1) since we are using only a constant amount of extra space.   
"""