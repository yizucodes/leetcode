# abcabcbb
#  l 
#    r
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # empty string
        if not s:
            return 0

        # set to track chars in window
        charSet = set()

        maxLen = 0
        l = 0

        # loop
        for r in range(len(s)):

            # check if curr char creates duplicate
            if s[r] in charSet:
                # shrink window until no more duplicate
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                    
            # add current char to set
            charSet.add(s[r])

            # max len
            maxLen = max(r - l + 1, maxLen)

        return maxLen
