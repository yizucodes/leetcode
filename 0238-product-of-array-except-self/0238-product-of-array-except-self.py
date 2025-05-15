class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        # Find prefix products, multiplying all numbers to the left
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Suffix products
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res

        
        