class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        position = m - 1

        for i in range(m - 1):
            if matrix[i][0] <= target and matrix[i + 1][0] > target:
                position = i
        
        for i in range(n):
            if matrix[position][i] == target:
                return True
        
        return False
            
