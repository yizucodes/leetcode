from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # p longer than s > return []
        if len(p) > len(s):
            return []

        # if same string return [0]
        if s == p:
            return [0]

        freqP = Counter(p)
        freqWin = Counter()
        res = []
        l = 0

        for r in range(len(s)):
            char = s[r]
            freqWin[char] += 1

            if freqWin == freqP:
                res.append(l)

            # shrink when window is greater
            while (r - l + 1) > len(p):
                removedChar = s[l]i
                freqWin[removedChar] -= 1
                l += 1
                if freqWin == freqP:
                    res.append(l)
              
        return res

