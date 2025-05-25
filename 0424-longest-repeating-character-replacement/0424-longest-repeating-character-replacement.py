from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        


        # if k is 0 return maxCharCount

        # if s is one letter, k is 0 then return 1

        maxCharCount = -1
        freqMapS = Counter(s)
        freqMapWin = Counter()
        l = 0

        # expand window when window size - maxCharCount <= ke
        for r in range(len(s)):
            char = s[r]
            freqMapWin[char] += 1
            maxCharCount = max(maxCharCount, freqMapWin[char])
            
        # shrink window window size - maxCharCount > k
            while (r - l + 1) - maxCharCount > k:
                removedChar = s[l]
                freqMapWin[removedChar] -= 1
                l += 1

        return (r - l + 1)


