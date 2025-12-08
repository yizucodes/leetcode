class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        # maxLen window
        maxLen = 0

        # charSet
        charSet = set()

        l = 0

        # iterate through letters until the end of the string
        for r in range(len(s)):
           
            char = s[r]

            # remove chars from left until no duplicate char
            while char in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(char)

            maxLen = max(r - l + 1, maxLen)

        return maxLen
