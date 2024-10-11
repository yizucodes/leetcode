class Solution:
    def firstUniqChar(self, s: str) -> int:

        if len(s) == 1:
            return 0

        freqMap = {}
        # find frequency of each char
        for char in s:
            if char not in freqMap:
                freqMap[char] = 1
            else:
                currFreq = freqMap[char]
                freqMap[char] = currFreq + 1

        # traverse through string and check if the char has frequency 1
        for i in range(len(s)):
            currChar = s[i]
            if freqMap[currChar] == 1:
                return i

        # every char is not unique
        return -1
        