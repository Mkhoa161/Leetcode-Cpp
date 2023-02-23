class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = True
        longestPalindrome_start = 0
        longestPalindrome_len = 1

        for end in range(0, n):
            for start in range(end - 1, -1, -1):
                if s[end] == s[start]:
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        palindrome_len = end - start + 1
                        if palindrome_len > longestPalindrome_len:
                            longestPalindrome_len = palindrome_len
                            longestPalindrome_start = start
        
        return s[longestPalindrome_start: longestPalindrome_start + longestPalindrome_len]
        

