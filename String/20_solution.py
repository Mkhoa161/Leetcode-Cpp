class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'{' : '}', '[' : ']', '(' : ')'}
        stack = []
        for char in s:
            if char in dict:
                stack.append(char)
            elif not stack or dict[stack.pop()] != char:
                return False
        return not stack
        
