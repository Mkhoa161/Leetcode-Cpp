class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        count = 0
        for val in nums:
          if val != 0:
            prod *= val
          else:
            count += 1

        if count > 1:
          return [0] * len(nums)

        for i, v in enumerate(nums):
          if count == 1:
            if v != 0:
              nums[i] = 0
            else:
              nums[i] = prod
          else:
            nums[i] = prod // nums[i]
        return nums

                
