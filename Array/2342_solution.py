from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort()
        dict = defaultdict(list)

        for num in nums:
            s = str(num)
            sum = 0
            for ch in s:
                sum += int(ch)
            dict[sum].append(num)
        
        
        max_sum = -1
        for key in dict:
            if len(dict[key]) < 2:
                continue
            for val in dict[key]:
                max_sum = max(max_sum, dict[key][-2] + dict[key][-1])
     
        return max_sum
                
