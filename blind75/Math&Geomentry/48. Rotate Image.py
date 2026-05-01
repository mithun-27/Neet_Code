#48. Rotate Image
"""You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000"""

#answer
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#example 1: 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
s.rotate(matrix)
print(matrix)  # Output: [[7,4,1],[8,5,2],[9,6,3]]
#example 2:
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s = Solution()  
s.rotate(matrix)
print(matrix)  # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

"""walkthrough:
1. We first reverse the matrix to flip it upside down. This can be done using the `reverse()` method, which modifies the list in place.
2. After reversing the matrix, we need to transpose it to achieve the final rotated state. Transposing the matrix involves swapping the elements at positions (i, j) with those at (j, i). We can do this by iterating through the upper triangle of the matrix (where j > i) to avoid swapping elements back to their original positions.
3. By performing these two steps (reversing and transposing), we effectively rotate the image by 90 degrees clockwise in place, without needing any additional space for another matrix.        
4. Finally, the modified matrix is printed to show the result of the rotation.  
This approach has a time complexity of O(n^2) due to the nested loops for transposing, and a space complexity of O(1) since we are modifying the matrix in place without using any extra space. 
""" 