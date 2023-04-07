class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        dict = {0: 1}
        ans = 0
        for val in nums:
            prefix_sum += val
            if prefix_sum - k in dict:
                ans += dict[prefix_sum - k]
                
            dict[prefix_sum] = dict.get(prefix_sum, 0) + 1
        return ans
