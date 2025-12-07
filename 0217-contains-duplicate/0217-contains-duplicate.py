class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # frequency of each number
        numFreq = {}

        for num in nums:
            if num in numFreq:
                return True
            numFreq[num] = 1
        
        return False


      
        