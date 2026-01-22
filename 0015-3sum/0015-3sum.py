class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if len 3 if sum is 0 then return [nums[0]]
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        elif len(nums) == 3 and sum(nums) != 0:
            return []

        # sort the list in ascending order
        nums.sort()

        res = []

        # do a for loop
        for i in range(len(nums)):
            l = i + 1  # Start after the fixed element
            r = len(nums) - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
    
            # nested while loop to find the two numbers that would add to 0 based on the fixed pointer
            while l < r:
                # if l + r == -nums[i]
                if nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1

                # Skip duplicates for l and r pointers
                while l < r and nums[l] == nums[l-1]:
                    l += 1

                while l < r and r > 0 and r < len(nums) and nums[r] == nums[r+1]:
                    r -= 1
                
        return res