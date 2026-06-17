#4. Median of Two Sorted Arrays
"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106"""

#answer
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

#example 1:
"""Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2."""
#example 2:
"""Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5."""

"""walkthrough:
1. We want to find the median of two sorted arrays, which means we need to find the middle element(s) of the combined sorted array.
2. We can use binary search to find the correct partition of the two arrays such that the left side of the partition contains the smaller half of the elements and the right side contains the larger half.
3. We will ensure that we always binary search on the smaller array to optimize the search process.
4. We will calculate the indices for the partition and check if the elements on the left side of the partition are less than or equal to the elements on the right side.
5. If the partition is correct, we can calculate the median based on whether the total number of elements is odd or even.
6. The time complexity of this algorithm is O(log(min(m, n))) where m and n are the lengths of the two arrays. The space complexity is O(1) since we are using only a constant amount of extra space.   
7. This approach is efficient and works well even when the two arrays have different sizes."""