class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        numSet = set(nums)

        res = []
        numTrack = 1

        for i in range(len(nums)):
            if numTrack not in numSet:
                res.append(numTrack)
            numTrack += 1

        return res
        