from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # if len p is greater than len s
        if len(p) > len(s):
            return []

        res = []
        freqMapWindow = Counter(p)

        # p is window
        for i in range(len(s) - len(p) + 1):
            endWindow = len(p)
            chunk = s[i : i + endWindow]
            freqMapChunk = Counter(chunk)
            if freqMapWindow == freqMapChunk:
                res.append(i)

        return res
