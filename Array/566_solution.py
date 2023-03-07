class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Check validity
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat 
            
        result = []
        line = []
        count = 0
        # for row -> for column
        for row in range(m):
            for col in range(n):
                line.append(mat[row][col])
                count += 1
                if count == c:
                    result.append(line)
                    count = 0
                    line = []
        return result
