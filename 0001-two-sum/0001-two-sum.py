class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numMap = {}
        # check for complement given by target - num
        for i in range(len(nums)):
            complement = target - nums[i]

            # if there is then return indices of complement and current num
            if complement in numMap:
                return [numMap[complement], i]
            else:
                numMap[nums[i]] = i

        return []


