

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        numMap = {}
        res = []

        # Add number to hashMap if its complement is not there (target - nums[i])
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in numMap:
                numMap[nums[i]] = i
            else:
                # Find index of complement
                res.append(numMap[complement])
                res.append(i)

        return res



 