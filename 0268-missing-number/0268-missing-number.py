class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        numSet = set(nums)

        numTrack = 0

        for i in range(len(nums)):
            if numTrack not in numSet:
                return numTrack
            numTrack += 1
        
        return numTrack
        