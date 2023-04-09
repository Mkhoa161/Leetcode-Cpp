class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        longest = ""
        longest_len = 0
        for i in range(0, len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if longest_len < right - left + 1: 
                    longest = s[left:right+1]
                    longest_len = right - left + 1
                left -= 1
                right += 1
            
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if longest_len < right - left + 1: 
                    longest = s[left:right+1]
                    longest_len = right - left + 1
                left -= 1
                right += 1
  
        return longest

        
        
