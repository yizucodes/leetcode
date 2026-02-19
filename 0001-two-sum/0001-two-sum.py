class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        # for each num 
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num

            if num in numMap:
                return [i, numMap[num]]
            
            numMap[complement] = i

        return []