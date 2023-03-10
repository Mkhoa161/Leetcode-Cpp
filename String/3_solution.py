class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_substring = 0
        dict = {}
        while right < len(s):
            char = s[right]
            if char in dict:
                left = max(left, dict[char] + 1)
            
            dict[char] = right    
            max_substring = max(max_substring, right - left + 1)
            right += 1
        
        return max_substring
