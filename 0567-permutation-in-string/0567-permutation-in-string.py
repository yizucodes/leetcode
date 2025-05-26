from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if same string return True
        if s1 == s2:
            return True

        # initialize vars
        l = 0
        freqS1 = Counter(s1)
        freqWin = Counter()

        # expand
        for r in range(len(s2)):
            char = s2[r]
            freqWin[char] += 1
            
            # shrink when freqS1 is not same as freqWindow
            while (r - l + 1) > len(s1):
                removedChar = s2[l]
                freqWin[removedChar] -= 1
                if freqWin == freqS1:
                    return True
                l += 1

            if freqWin == freqS1:
                return True

        return False