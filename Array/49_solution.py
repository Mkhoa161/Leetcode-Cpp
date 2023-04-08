class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            sort = tuple(sorted(word))
            map[sort] = map.get(sort, []) + [word]
        return [i for i in map.values()]
