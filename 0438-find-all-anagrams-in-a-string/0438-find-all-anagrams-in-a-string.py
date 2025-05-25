from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # p is longer than s then return []
        if len(p) > len(s):
            return []

        # if same strings then return [0]
        if s == p:
            return [0]

        res = []
        freqWindow = Counter()
        freqP = Counter(p)
        l = 0

        # expand if the frequency of char in window is not the same as frequency of char in p
        for r in range(len(s)):
            char = s[r]
            freqWindow[char] += 1

        # shrink when window length is bigger than len(p)
            while (r - l + 1) > len(p):
                removedChar = s[l]
                freqWindow[removedChar] -= 1
                l += 1
            
            # if length of window is the same
            # check if freqWindow == freqP
            if (r - l + 1) == len(p) and Counter(freqWindow) == Counter(freqP):
                res.append(l)

        return res
