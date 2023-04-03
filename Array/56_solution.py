class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals = sorted(intervals, key=lambda x : x[0])
        
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:

                if intervals[i][1] <= intervals[i+1][1]:
                    list_to_add = [intervals[i][0], intervals[i+1][1]]
                    intervals.remove(intervals[i])
                    intervals.remove(intervals[i])
                    intervals.insert(i, list_to_add)

                else:
                    intervals.remove(intervals[i+1])
            
            else:
                i += 1
        
        return intervals
