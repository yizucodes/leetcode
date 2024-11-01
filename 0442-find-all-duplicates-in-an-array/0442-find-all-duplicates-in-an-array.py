from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # freqMap
        freqMap = Counter(nums)
        res = []

        # Traverse freqMap.items()
        for key, value in freqMap.items():
            if value == 2:
                res.append(key)

        return res
        