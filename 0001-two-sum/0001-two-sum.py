from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
            
        numMap = {}
        for i in range(len(nums)):
            currNum = nums[i]
            # check if complement exists
            # if exists return [iNum, iComplment]
            complement = target - currNum
            if complement in numMap:
                return [i, numMap[complement]]

            # store index
            numMap[currNum] = i

        # No answer
        return []