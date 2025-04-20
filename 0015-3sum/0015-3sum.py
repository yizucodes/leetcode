class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # length 3 and all 0
        if len(nums) == 3 and sum(nums) == 0:
            return [[0,0,0]]
        if len(nums) == 3 and sum(nums) != 0:
            return []
        # what is there are only zeros on multiples of 3?

        # fix one number and then you have a problem left