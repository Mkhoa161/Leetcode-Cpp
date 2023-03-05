class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = abs(nums[i])
        lst = [val * val for val in nums]
        lst.sort()
        return lst
