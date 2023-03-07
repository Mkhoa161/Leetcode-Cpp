class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)

        result = []
        dic = {}
        for val in nums1:
            dic[val] = dic.get(val, 0) + 1

        for val in nums2:
            if val in dic and dic[val] > 0:
                result.append(val)
                dic[val] -= 1
        return result
         
