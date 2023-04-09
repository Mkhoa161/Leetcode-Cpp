class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        st = set()
        res = []
        for i in range(len(s) - 9):
            word = s[i:i+10]
            if word in st and word not in res:
                res.append(word)
                continue
            st.add(s[i:i+10])
        return res
