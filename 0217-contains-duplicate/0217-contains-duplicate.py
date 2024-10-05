class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if one number return false as no repetition
        if len(nums) == 1:
            return False

        # create map
        numMap = {}

        # add number to map if first occurrence
        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                return True
        
        # Every num in array is unique
        return False