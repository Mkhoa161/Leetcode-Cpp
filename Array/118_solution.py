class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        line = []
        result = [[1]]
        prev = [1]
        size = 0

        for i in range(1, numRows):
            size = i + 1
            index = 0
            while index < size:
                if index == 0 or index == size - 1:
                    line.append(1)
                else:
                    line.append(prev[index] + prev[index - 1])
                index += 1
                
            prev = line
            result.append(line)
            line = []
        return result
            
