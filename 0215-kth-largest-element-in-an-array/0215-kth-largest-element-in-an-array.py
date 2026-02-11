class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    
        # Sort in Descending
        nums.sort(reverse = True)
        
        # Return sorted nums[k - 1]

        return nums[k - 1]
        