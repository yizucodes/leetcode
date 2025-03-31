class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # empty string
        if len(s) == 0:
            return 0

        # one letter
        if len(s) == 1:
            return 1

        currMax = 0
        l = 0
        r = 0

        charSet = set()
        currLen = 0
        while r < len(s):
            currChar = s[r]
            # add to set if letter not seen --> move right
            if currChar not in charSet:
                charSet.add(currChar)
                r += 1
                currLen += 1
                currMax = max(currMax, currLen)
            else:
                # shrink until no duplicates

                # while the left pter letter is in the set, then remove letter from set and decrement currMax
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
                    currLen -= 1

            print('left', l)
            print('right', r)
            print("set ", charSet)
            print("currMax ", currMax)
            # if seen pop it --> move left

        # expand when substring is w/o duplicates
        return currMax

        abcabcbb