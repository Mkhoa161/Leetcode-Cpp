class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        def intersection(lst1, lst2):
            temp = set(lst2)
            res = [val for val in lst1 if val in temp]
            return res

        result = nums[0]
        for i in range(1, len(nums)):
            result = intersection(result, nums[i])
        result.sort()
        return result

