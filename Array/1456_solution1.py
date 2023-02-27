class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        lst = []

        # Start building the prefix_sum list
        if s[0] in vowels:
            lst.append(1)
        else:
            lst.append(0)

        for i in range(1, len(s)):
            if s[i] in vowels:
                lst.append(lst[-1] + 1)
            else:
                lst.append(lst[-1])

        # sliding window
        end = 0
        start = 0
        res = 0

        while end < len(s):
            if end - start + 1 == k:
                if end - k >= 0:
                    res = max(res, lst[end] - lst[end - k])
                else:
                    res = max(res, lst[end])
                start += 1
            end += 1
        return res
