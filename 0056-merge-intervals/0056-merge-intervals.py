class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by their start time
        # This ensures we process intervals in chronological order
        # Example: [[2,6],[1,3],[8,10]] becomes [[1,3],[2,6],[8,10]]
        intervals.sort(key = lambda i : i[0])
        
        # Step 2: Initialize output with the first interval
        # We'll build our result by comparing each interval with the last merged interval
        output = [intervals[0]]

        # Step 3: Iterate through remaining intervals starting from index 1
        for start, end in intervals[1:]:
            # Get the end time of the most recently added interval in our output
            lastEnd = output[-1][1]

            # Step 4: Check if current interval overlaps with the last interval in output
            # Overlap occurs when: current_start <= last_end
            # Example: [1,3] and [2,6] overlap because 2 <= 3
            if start <= lastEnd:
                # Merge intervals by extending the end time of the last interval
                # Take the maximum end time to cover both intervals completely
                # Example: merge [1,3] and [2,6] -> [1,6] (max(3,6) = 6)
                output[-1][1] = max(lastEnd, end)
            else:
                # No overlap found - add current interval as a separate interval
                # Example: [1,6] and [8,10] don't overlap (8 > 6)
                output.append([start, end])
        
        # Return the merged intervals
        return output