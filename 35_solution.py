class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target and nums[i + 1] > target:
                return i + 1
            
