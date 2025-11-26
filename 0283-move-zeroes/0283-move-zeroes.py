class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            return nums

        write = 0
        
        # read pointer reads non-zero
        

        # if read pter reads non-zero element, write pointer = read value
        # write += 1

        # once read pter traverses entire array, write marks 0 the remaining values

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write] = nums[i]
                write += 1

        while write < len(nums):
            nums[write] = 0
            write += 1

        return nums


        



   
        