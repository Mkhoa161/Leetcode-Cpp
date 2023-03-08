class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for ch in magazine:
            dict[ch] = dict.get(ch, 0) + 1
        
        for ch in ransomNote:
            if ch not in dict or dict[ch] == 0:
                return False
            elif ch in dict:
                dict[ch] -= 1
        
        return True
