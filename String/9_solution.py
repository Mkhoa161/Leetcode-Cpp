class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        b = str(x)
        if a[::-1] == b:
            return True
        return False
