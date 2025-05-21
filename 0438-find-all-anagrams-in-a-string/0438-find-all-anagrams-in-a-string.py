from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        res = []

        # init freqmap for window and p (char : freq)
        freqMapP = Counter(p)
        freqMapWindow = Counter()

        l = 0
        
        # sliding window
        for r in range(len(s)):
            
            # append char p[r] to window
            # update window map
            freqMapWindow[s[r]] += 1
            
            if (r - l + 1) > len(p):
            # shrink left by 1
            # update window map
                freqMapWindow[s[l]] -= 1
                l += 1

            if (r - l + 1) == len(p):
                if freqMapWindow == freqMapP:
                    res.append(l)

        return res