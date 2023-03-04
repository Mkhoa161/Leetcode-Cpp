# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            middle = left + (right - left) // 2
            if isBadVersion(middle): 
                if not isBadVersion(middle - 1):
                    return middle
                else: 
                    right = middle - 1
            else:
                left = middle + 1
        
            
