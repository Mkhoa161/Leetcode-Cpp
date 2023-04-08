class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = {s[i] : i for i in range(len(s))}
        i = 0
        res = []
        while i < len(s):
            end, j = hash_map[s[i]], i + 1
            while j < end:
                if hash_map[s[j]] > end:
                    end = hash_map[s[j]]
                j += 1
            res.append(end - i + 1)
            i = end + 1 
        return res
