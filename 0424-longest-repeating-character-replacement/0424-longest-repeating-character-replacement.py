class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #Initialize left pointer (l), maxCount = 0, empty freq map
        l = 0
        maxCount = 0
        freqMap = defaultdict(int)

#Initialize result (maxLen) = 0
        maxLen = 0

#Loop through s with right pointer (r):
   # - Increment count of s[r] in freq map
    # - Update maxCount if needed

        for r in range(len(s)):
            freqMap[s[r]] += 1
            maxCount = max(maxCount, freqMap[s[r]])
    
    # - If (window size - maxCount) > k:
            windowSize = r - l + 1
            if (windowSize - maxCount) > k:
    # - Shrink window from the left (decrement s[l] in freq map, move l forward)
                freqMap[s[l]] -= 1
                l += 1
        
            maxLen = max(maxLen, r - l + 1)

    # - Update maxLen as max(maxLen, current window size)

    # Return maxLen

        return maxLen
        