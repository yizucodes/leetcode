class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            # Skip duplicate fixed values (minimal fix #1)
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # No need to check "not in result" anymore!
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate left values (minimal fix #2)
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    # Skip duplicate right values (minimal fix #3)
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                        
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result

# Only 3 lines added to fix timeout:
# 1. Skip duplicate i values: if i > 0 and nums[i] == nums[i-1]: continue
# 2. Skip duplicate left values after finding match
# 3. Skip duplicate right values after finding match
#
# Now it's O(n²) instead of O(n³) and handles large inputs!
# Removes the slow "not in result" check entirely.