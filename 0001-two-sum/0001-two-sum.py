class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2 numbers
        if len(nums) == 2 and nums[0] + nums[1] == target:
            return [0, 1]

        res = []
        numMap = {}

        # number: index
        for i in range(len(nums)):
            currNum = nums[i]
            complement = target - currNum
            # if number does not add to target
            if complement not in numMap:
                numMap[currNum] = i
            else:
                return [i, numMap[complement]]


        
        # no solution
        return []