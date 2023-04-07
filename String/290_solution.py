class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split()
        if len(lst) != len(pattern):
            return False
        
        dict1 = {}
        dict2 = {}
        track = []
        for i in range(len(lst)):
            track.append((pattern[i], lst[i]))
            if pattern[i] in dict1 and dict1[pattern[i]] != lst[i]:
                return False
            if lst[i] in dict2 and dict2[lst[i]] != pattern[i]:
                return False
            dict1[pattern[i]] = lst[i]
            dict2[lst[i]] = pattern[i]

        
        left = 0
        right = len(pattern) - 1
        while left <= right:
            if track[left][0] == track[right][0] and track[left][1] != track[right][1]:
                return False
            if track[left][0] != track[right][0] and track[left][1] == track[right][1]:
                return False
            left += 1
            right -= 1
        return True
