class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lst = []
        count = 0
        for i in range(len(nums)):
            if nums[i] in lst:
                nums[i] = nums[-1] + 1
            else:
                lst.append(nums[i])
                count += 1
        nums.sort()
        return count
        
