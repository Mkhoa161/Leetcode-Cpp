class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        HashMap = {}
        for ch, word in zip(pattern,s.split()):
            if ch not in HashMap:
                HashMap[ch] = word
            else:
                if HashMap[ch] != word:
                    return False
        return False if len(set(HashMap.values())) != len(HashMap) else True
