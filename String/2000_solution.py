class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix_sum = [word[0]]
        for i in range(1, len(word)):
            prefix_sum.append(word[i] + prefix_sum[i-1]) 

        for i in range(len(prefix_sum)):
            if prefix_sum[i][0] == ch:
                return prefix_sum[i] + word[i+1:]
        return word
        
