class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if nums[i] in numMap:
                return [numMap[nums[i]], i]
            else:
                numMap[comp] = i

        
        return