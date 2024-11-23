class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        merged = []

        # Sort the intervals by their start times
        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
        
            if len(merged) == 0 or merged[-1][1] < interval[0]:
                # how to access interval + 1, next array?
                merged.append(interval)
            else:
                # Overlap so merge intervals
                mergedEnd = merged[-1][1]
                endInterval = interval[1]
                merged[-1][1] = max(mergedEnd, endInterval)
        return merged
               

        