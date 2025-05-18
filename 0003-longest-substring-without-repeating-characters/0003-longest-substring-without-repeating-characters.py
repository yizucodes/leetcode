class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # empty string --> 0
        if len(s) == 0:
            return 0

        # one letter -> 1
        if len(s) == 1:
            return 1
        
        maxLen = 0
        currLen = 0
        left = 0

        currChars = set()
        for right in range(len(s)):

            # if dups, shrink until there is no dups
            while s[right] in currChars:
                currChars.remove(s[left])
                left += 1
                    
            currLen = right - left + 1
            if currLen > maxLen:
                maxLen = currLen
            currChars.add(s[right])

        return maxLen



