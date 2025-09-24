from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Counter
        freqMap = Counter(nums)

        for freq in freqMap.values():
            # if any freq is > 1 return True
            if freq > 1:
                return True
        
        return False