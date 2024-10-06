class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # nums is one or k is 0 return false
        if len(nums) == 1 or k == 0:
            return False
        
        numSet = {}

        for i in range(len(nums)):
            if nums[i] in numSet and i - numSet[nums[i]] <= k:
                return True
            numSet[nums[i]] = i

            if len(numSet) > k:
                del numSet[nums[i - k]]
        return False   

