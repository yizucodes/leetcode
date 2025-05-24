from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        res = []

        # freqMapP
        freqMapP = Counter(p)

        # winMap
        winMap = Counter()

        l = 0

        # sliding window
            # check if winMap = freqMapP
                # append the starting index giving by left

        for r in range(len(s)):
            winMap[s[r]] += 1

            if winMap == freqMapP:
                res.append(l)
            
            # shrink windowLen > len(freqMapP)
            # check for equality
            # move left += 1
            while (r - l + 1) > len(p):
                winMap[s[l]] -= 1
                if winMap == freqMapP:
                    res.append(l)
                l += 1
            
        return res
        
