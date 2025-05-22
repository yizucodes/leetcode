class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        # init winSet, l
        winSet = set()
        l = 0

        # maxLen
        maxLen = 0

        # sliding window
        for r in range(len(s)):
            
            # shrink it when a letter in the window is in the set, shrink until there is no duplicate letters
            while s[r] in winSet:
                winSet.remove(s[l])
                l += 1
            
            # check if current length (r - l + 1) > maxLen
            if (r - l + 1) > maxLen:
                maxLen = r - l + 1

            # add newly added char to set
            winSet.add(s[r])

        return maxLen