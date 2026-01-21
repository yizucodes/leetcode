class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        
        for i in range(len(nums)):
            # if num[i] in numMap --> return indices
            if nums[i] in numMap:
                return [i, numMap[nums[i]]]

            # otherwise add complement t - num : i to numMap
            complement = target - nums[i]
            numMap[complement] = i

        return []




