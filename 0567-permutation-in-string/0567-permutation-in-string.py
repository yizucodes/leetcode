from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) == 1 and s1 in s2 or s1 == s2:
            return True

        # init map for s1
        s1Map = Counter(s1)
        l = 0
        winFreqMap = Counter()

        # move right
        for r in range(len(s2)):

            # add s2[right] to windowFreqMap
            winFreqMap[s2[r]] += 1


            # check if lenght of 1 == s2
                # winFreq == s1Freq --> return Tru
            if len(s1) == (r - l + 1):
                if winFreqMap == s1Map:
                    return True
            
            # shrink len(window) > len(s1)
            while (r - l + 1) > len(s1):
                # remove s[l] from winFreq
                winFreqMap[s2[l]] -= 1
                # delete from map
                if winFreqMap[l] == 0:
                    del winFreqMap[l]
                l += 1

        return False
                




            