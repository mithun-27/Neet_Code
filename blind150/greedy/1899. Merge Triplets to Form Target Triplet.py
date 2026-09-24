#1899. Merge Triplets to Form Target Triplet
"""A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.

 

Example 1:

Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4],[2,7,5]]
The target triplet [2,7,5] is now an element of triplets.
Example 2:

Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false
Explanation: It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.
Example 3:

Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
The target triplet [5,5,5] is now an element of triplets.
 

Constraints:

1 <= triplets.length <= 105
triplets[i].length == target.length == 3
1 <= ai, bi, ci, x, y, z <= 1000"""


#answer:
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False
        for t in triplets:
            x |= (t[0] == target[0] and t[1] <= target[1] and t[2] <= target[2])
            y |= (t[0] <= target[0] and t[1] == target[1] and t[2] <= target[2])
            z |= (t[0] <= target[0] and t[1] <= target[1] and t[2] == target[2])
            if x and y and z:
                return True
        return False

#example:
"""Input
triplets =
[[2,5,3],[1,8,4],[1,7,5]]
target =
[2,7,5]
Output
true
Expected
true"""

#example:
"""Input
triplets =
[[3,4,5],[4,5,6]]
target =
[3,2,5]
Output
false
Expected
false
"""


"""Walkthrough:
1. We want to determine whether it is possible to obtain the `target` triplet by merging some of the given triplets.
2. When two triplets are merged, the resulting triplet takes the maximum value at each index.
3. Therefore, any triplet containing a value greater than the corresponding value in the target cannot be part of a valid merge because that value can never be reduced.
4. To form the target triplet, we need to find triplets that can individually contribute the target value for each position.
5. We maintain three boolean variables:
   - `x` → whether we found a valid triplet contributing `target[0]`.
   - `y` → whether we found a valid triplet contributing `target[1]`.
   - `z` → whether we found a valid triplet contributing `target[2]`.
6. For each triplet `t`, we check whether its first value equals `target[0]` while its other values do not exceed the corresponding target values.
7. If such a triplet exists, then it can safely contribute the first coordinate of the target, so we set `x = True`.
8. Similarly, we check whether the triplet can contribute the second coordinate of the target and update `y`.
9. We also check whether the triplet can contribute the third coordinate of the target and update `z`.
10. Since merging takes the maximum value at each position, having separate triplets that contribute each target coordinate is sufficient to construct the target.
11. After processing a triplet, if `x`, `y`, and `z` are all `True`, then we already have all required components of the target.
12. In that case, we can immediately return `True` because merging those valid triplets will produce the target triplet.
13. If the loop finishes and at least one of `x`, `y`, or `z` is still `False`, then some target coordinate cannot be obtained.
14. Therefore, it is impossible to form the target triplet, and we return `False`.
15. The key insight is that we only need to verify the existence of valid contributors for each target coordinate rather than explicitly performing all possible merges.
16. The time complexity is `O(n)` because each triplet is processed once, and the auxiliary space complexity is `O(1)` since only three boolean variables are used."""