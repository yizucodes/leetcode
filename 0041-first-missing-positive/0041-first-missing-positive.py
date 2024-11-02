class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # Create a set with numbers
        numSet = set(nums)

        # Start from 1
        numTrack = 1

        # Count from 1 and check if number is in set
        for num in range(len(nums)):
            if numTrack not in numSet:
                return numTrack
            numTrack += 1

        return numTrack
        