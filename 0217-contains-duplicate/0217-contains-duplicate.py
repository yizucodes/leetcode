class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freqMap = {}

        for num in nums:
            if num in freqMap:
                return True
            freqMap[num] = 0
        
        return False

        