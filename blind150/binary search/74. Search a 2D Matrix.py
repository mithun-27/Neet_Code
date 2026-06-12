#74. Search a 2D Matrix
"""You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104"""

#answer
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False
    

#example 1:
"""Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true  """
#example 2:
"""Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false  """  

"""walkthrough:
1. We start by determining the number of rows (ROWS) and columns (COLS) in the matrix. This will help us calculate the total number of elements in the matrix, which is ROWS * COLS.
2. We initialize two pointers, l and r, to represent the left and right boundaries of our search space. Initially, l is set to 0 (the index of the first element in the flattened matrix) and r is set to ROWS * COLS - 1 (the index of the last element in the flattened matrix).
3. We enter a while loop that continues as long as l is less than or equal to r. This loop will help us narrow down our search space until we find the target or determine that it does not exist in the matrix.
4. Inside the loop, we calculate the middle index m using the formula l + (r - l) // 2. This formula helps prevent potential overflow issues that can arise with large indices.
5. We then convert the middle index m back into row and column indices using the formulas row = m // COLS and col = m % COLS. This allows us to access the corresponding element in the matrix.
6. We compare the value at matrix[row][col] with the target. If the value is less than the target, it means that the target must be in the right half of the current search space (excluding m), so we update l to m + 1. If the value is greater than the target, it means that the target must be in the left half of the current search space (excluding m), so we update r to m - 1. If the value is equal to the target, we have found the target and we return True.
7. If the loop terminates without finding the target, we return False to indicate that the target does not exist in the matrix.
This algorithm efficiently searches for the target in a sorted 2D matrix with a time complexity of O(log(m * n)) and a space complexity of O(1).
"""