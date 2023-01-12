class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        size = len(nums)
        if size % 2 == 0:
            return (nums[size//2] + nums[-1 + size//2])/2
        else:
            return nums[(size - 1) // 2]
