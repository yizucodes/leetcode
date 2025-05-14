class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if there are two numbers in array --> check if the 2 nums add to target
        if len(nums) == 2 and nums[0] + nums[1] == target:
            return [0, 1]

        # map to check
        numMap = {}

        # iterate through array
        for i in range(len(nums)):
            # complement --> target - nums[i]
            complement = target - nums[i]

            # check complement is in the map
            if complement in numMap:
                # if yes, return [indComplement, indCurrNum --> inded of nums[i] ]
                return [i, numMap[complement]]
            else:
                numMap[nums[i]] = i

        return []
        





