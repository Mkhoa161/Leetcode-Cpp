class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                n = n - 1
                nums[i] = 101
        nums.sort()
        return n
