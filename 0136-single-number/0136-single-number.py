from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Freq map
        freqMap = Counter(nums)

        # Return number with freq of 1
        for key, val in freqMap.items():
            if val == 1:
                return key

        return None