class Solution:
    def findTheWinner(self, n, k):
        result, start = [i for i in range(1,n+1)], 0
        while len(result)>1:
            loser = (start+k-1)%len(result)
            del result[loser]
            start = loser if loser<=len(result) else 0
        return result[0]
