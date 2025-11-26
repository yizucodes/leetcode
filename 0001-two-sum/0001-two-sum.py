class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        # store complement (target - num): index

        for i in range(len(nums)):
            complement = target - nums[i]

            # if there is complement
            if nums[i] in numMap:
                return [i, numMap[nums[i]]]
            # no pair
            else:
                # why is it that you numMap[nums[i]] = i?
                numMap[complement] = i 
        return []