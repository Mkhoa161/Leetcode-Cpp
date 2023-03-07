class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # create dictionary with subtraction is key and index is item
        dict = {}
        for i in range(len(numbers)):
            if numbers[i] in dict:
                return [dict[numbers[i]] + 1, i + 1] 
            dict[target - numbers[i]] = i 
