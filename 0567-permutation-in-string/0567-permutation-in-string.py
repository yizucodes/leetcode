from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # init map for s1
        s1Map = Counter(s1)
        l = 0
        winFreqMap = Counter()

        # move right
        for r in range(len(s2)):

            # add s2[right] to windowFreqMap
            winFreqMap[s2[r]] += 1
            
            # shrink len(window) > len(s1)
            while (r - l + 1) > len(s1):
                # remove s[l] from winFreq
                winFreqMap[s2[l]] -= 1
                l += 1

            if len(s1) == (r - l + 1):
                if winFreqMap == s1Map:
                    return True

        return False
                




            