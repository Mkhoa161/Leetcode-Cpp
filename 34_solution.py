class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i in range(len(nums)):
            if nums[i] == target:
                if i == len(nums) - 1:
                    return [i, i]
                if nums[i+1] != target:
                    return [i, i]
                lst.append(i)
                while len(nums) > i + 1 and nums[i+1] == target:
                    i += 1
                lst.append(i)
                return lst
        return [-1, -1]
