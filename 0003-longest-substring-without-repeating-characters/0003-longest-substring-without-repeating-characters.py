class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # check for empty
        if len(s) == 0:
            return 0

        # check for length 1
        if len(s) == 1:
            return 1

        # init set in currWindow
        l = 0
        currMax = 0
        winSet = set()

        # sliding window
        for r in range(len(s)):

            # shrink if there is a duplicate
            while s[r] in winSet:
                winSet.remove(s[l])
                l += 1
            # check if current lenght (r - l + 1) > currMax
                if (r - l + 1) > currMax:
                    currMax = r - l + 1
            
            winSet.add(s[r])
        
        return currMax




