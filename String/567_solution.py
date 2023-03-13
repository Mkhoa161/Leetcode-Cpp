class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        def checkPermutation(s1, s2):
            if Counter(s1) == Counter(s2):
                return True
            return False
        
        if len(s2) < len(s1):
            return False

        left = 0
        right = len(s1) - 1

        while right < len(s2):
            if checkPermutation(s1, s2[left: right + 1]):
                return True
            left += 1
            right += 1

        return False
