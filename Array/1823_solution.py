class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        stack = [x for x in range(1, n + 1)]
        j = 0
        while len(stack) > 1:
            for i in range(k):
                if j > len(stack) - 1:
                    j = 0
                j += 1
            j -= 1
            remover = stack[j]
            stack.remove(remover)
        return stack[0]
            
            
            
            

