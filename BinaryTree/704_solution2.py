class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search_(nums, low, high):
            middle = (high+low)//2
            if low > high:
                return -1
            elif nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return search_(nums, middle+1, high)
            else:
                return search_(nums, low, middle-1)
        return search_(nums, 0, len(nums) - 1)
