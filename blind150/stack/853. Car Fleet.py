#853. Car Fleet
"""There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

Output: 3

Explanation:

The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Example 2:

Input: target = 10, position = [3], speed = [3]

Output: 1

Explanation:

There is only one car, hence there is only one fleet.
Example 3:

Input: target = 100, position = [0,2,4], speed = [4,2,1]

Output: 1

Explanation:

The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
 

Constraints:

n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106"""

#answer
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            currCar = pair[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets
    
#example 1:
#Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
#Output: 3  
#example 2:
#Input: target = 10, position = [3], speed = [3]    
#Output: 1
#example 3: 
#Input: target = 100, position = [0,2,4], speed = [4,2,1]
#Output: 1      

"""walkthrough :
1. We create a list of pairs (position, speed) for each car using the zip function and sort it in reverse order based on the position. This allows us to process the cars starting from the one closest to the target.  
2. We initialize a variable fleets to 1, which will count the number of car fleets. We also calculate the time it takes for the first car (the one closest to the target) to reach the target and store it in prevTime. This is calculated as (target - position) / speed for that car. 
3. We iterate through the sorted list of pairs starting from the second car (index 1). For each car, we calculate the time it takes for that car to reach the target in the same way as we did for the first car and store it in currTime.  
4. We compare currTime with prevTime. If currTime is greater than prevTime, it means that the current car cannot catch up to the fleet ahead of it and will form a new fleet. In this case, we increment the fleets count by 1 and update prevTime to currTime. If currTime is less than or equal to prevTime, it means that the current car will catch up to the fleet ahead of it and will be part of the same fleet, so we do not increment the fleets count.    
5. After iterating through all the cars, we return the total number of fleets.  
6. The time complexity of this solution is O(n log n) due to the sorting step, and the space complexity is O(n) for storing the pairs.
"""