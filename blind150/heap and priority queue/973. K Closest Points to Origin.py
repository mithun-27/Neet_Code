#973. K Closest Points to Origin
"""Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 104
-104 <= xi, yi <= 104"""

#answer
class Solution:
    def kClosest(self, points, k):
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        def partition(l, r):
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])
            i = l
            for j in range(l, r):
                if euclidean(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]

#example 1:
solution = Solution()
points = [[1,3],[-2,2]]
k = 1
print(solution.kClosest(points, k)) #Output: [[-2,2]]
#example 2:
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(solution.kClosest(points, k)) #Output: [[3,3],[-2,4]]


"""walkthrough:
1. Define a lambda function `euclidean` to calculate the squared Euclidean distance of a point from the origin.
2. Define a `partition` function that rearranges the points based on their distance to the origin, using the last point as the pivot.
3. Initialize two pointers `L` and `R` to represent the current range of points being considered, and set `pivot` to the length of the points list.
4. Use a while loop to repeatedly partition the points until the pivot index equals `k`.
5. Inside the loop, call the `partition` function and update the pointers `L` and `R` based on the pivot index.
6. Once the loop exits, return the first `k` points from the list, which are the closest to the origin.     
7. The algorithm has an average time complexity of O(n) due to the partitioning process, making it efficient for large datasets."""