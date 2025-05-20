class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # initialize vars
        numOnes = 0
        l = 0
        maxLen = 0

        # expand window
        for r in range(len(nums)):
            if nums[r] == 1:
                numOnes += 1

            # check if window is valid
            while (r - l + 1) - numOnes > k:
                if nums[l] == 1:
                    numOnes -= 1
                l += 1
                    
            # update maxLen if window is valid
            maxLen = max(maxLen, r - l + 1)

        return maxLen