class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # one element -> false
        freqMap = {}
        for num in nums:
            # in map return True
            if num in freqMap:
                return True

            # add to map
            freqMap[num] = 1

        
        return False
            
        