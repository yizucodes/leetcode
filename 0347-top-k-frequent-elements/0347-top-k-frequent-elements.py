
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # one item return nums
        if len(nums) == 1:
            return nums

        # create dictionary for each unique number in nums
        numDict = {}
        for nume in nums:
            if nume not in numDict:
                numDict[nume] = 1
            else:
                numDict[nume] += 1

        # Sort dictionary items by value (freq) from high to low
        sorted_items = sorted(numDict.items(), key = lambda x: x[1], reverse=True)

        # Return k most requent elements
        return [item[0] for item in sorted_items[:k]]

        