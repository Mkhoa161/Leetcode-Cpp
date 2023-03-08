class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = set()
        n = set()
        for ch in s:
            if ch in m:
                n.add(ch)
            m.add(ch)
        
        for i in range(len(s)):
            if s[i] not in n:
                return i
        
        return -1

            
