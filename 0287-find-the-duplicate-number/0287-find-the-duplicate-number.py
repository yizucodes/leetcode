from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # map and return number with frequency of 2
        
        numMap = Counter(nums)

        for num in numMap:
            if numMap[num] >= 2:
                return num

        return -1