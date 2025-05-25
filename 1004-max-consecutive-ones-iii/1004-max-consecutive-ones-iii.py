from collections import Counter
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1 and nums[0] == 1:
            return 1

        maxLen = -1
        l = 0
        freqMapWin = Counter()

        # expand window
        for r in range(len(nums)):
            num = nums[r]
            freqMapWin[num] += 1

            # shrink window when winLen - numOnes > k
            while freqMapWin[0] > k:
                removedNum = nums[l]
                freqMapWin[removedNum] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)
                
        return maxLen
        


