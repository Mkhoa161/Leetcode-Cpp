class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def longestPrefixTwo(word1, word2):
            if len(word1) > len(word2):
                n = len(word2)
            else:
                n = len(word1)
            
            while n != 0:
                if word1[0: n] == word2[0: n]:
                    return word1[0: n]
                n -= 1
            return ""
        
        longestPrefix = strs[0]
        for i in range(len(strs) - 1):
            longestPrefix = longestPrefixTwo(longestPrefix, strs[i + 1])
        return longestPrefix

        
