class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = dict()
        for index, value in enumerate(nums):
            ans = target- value
		    #ans = the one we are searching 
		    # we are keeping all the elements on dict called                 elements to check whether we have seen the ans                 value before by using dic
            if ans in elements:
                return [elements[ans], index]
        
		    #adding current value to dic if ans is not in the                elements we have seen before
            elements[value] = index
    
	        #we are returning empty list 
        return []
