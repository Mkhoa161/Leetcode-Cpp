class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict = Counter(nums)
        sum = 0
        for val in nums:
            if dict[val] == 1:
                sum += val
        
        return sum
