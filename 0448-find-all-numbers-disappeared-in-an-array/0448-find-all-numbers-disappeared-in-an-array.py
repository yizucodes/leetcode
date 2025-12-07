class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numSet = set(nums)

        # n == len of array

        # check if number is in 
        return [num for num in range(1, len(nums) + 1) if num not in numSet]

