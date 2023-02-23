class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lst = []
        for i in nums:
            if i in lst:
                lst.remove(i)
            else:
                lst.append(i)
        return lst[0]
            
