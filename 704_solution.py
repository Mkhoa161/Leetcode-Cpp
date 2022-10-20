class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while high - low > 1:
            middle = (high + low) // 2
            if nums[middle] < target:
                low = middle + 1
            else:
                high = middle
        
        if nums[low] == target:
            return low
        elif nums[high] == target:
            return high
        else:
            return -1
        
