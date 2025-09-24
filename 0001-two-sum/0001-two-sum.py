class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMap = {}

        for i in range(len(nums)):
            currNum = nums[i]
            complement = target - currNum
            
            if currNum in numMap:
                return [i, numMap[currNum]]
            
            numMap[complement] = i

        return []