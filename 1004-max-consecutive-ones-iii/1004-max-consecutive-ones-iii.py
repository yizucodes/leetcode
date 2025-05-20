class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        if k == 0 and sum(nums) == 0:
            return 0

        # left pointer
        l = 0

        # maxLen
        maxLen = 0

        numOnes = 0

        # expand window
        for r in range(len(nums)):
            numOnes += (nums[r] == 1)

            # check if window is valid
            # maxCount = max(maxCount, freqMap[nums[r]])
            # numOnes = max(numOnes, nums[r])

            # num substitutions in window is greater than allowed k
            while (r - l + 1) - numOnes > k:
                if nums[l] == 1:
                    numOnes -= 1
                l += 1

            # update maxLen if window is valid
            maxLen = max(maxLen, r - l + 1)

        return maxLen

