class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numMap = {}
        
        for i in range(len(nums)):
            num = nums[i]
            if num in numMap:
                return [i, numMap[num]]
            # calc comp and store the current index
            complement = target - num
            numMap[complement] = i

        return []



        