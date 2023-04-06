class Solution:
    def longestPalindrome(self, s: str) -> int:
      if len(s) == 1:
          return 1

      dict = Counter(s)  
      longest = 0
      odd = 0

      for val in dict.values():
        if val > 1:
          if val % 2 == 0:
            longest += val
          else:
            longest += val - 1
            odd += 1
        else:
          odd += 1
      
      return longest + (odd > 0)
