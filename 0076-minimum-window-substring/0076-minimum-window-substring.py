from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if len t > len s return ""
        if s == t:
            return t
        
        # tFreq
        tFreq = Counter(t)

        # windowFreq
        winFreq = Counter()

        res = ""
        have = 0
        need = len(tFreq)
        l = 0

        # expand window until windowFreq has all the letters in freqT
        # when winFreq[char] == tFreq[char] --> have += 1

        for r in range(len(s)):
            char = s[r]
            winFreq[char] += 1
            
            if winFreq[char] == tFreq[char]:
                have += 1

            # shrink window while there are still all the letters in window
            # if remove one of the chars in tFreq, have - 1

            while have == need:
            
                if res == "":
                    res = s[l:r+1]
                
                elif (r - l + 1) < len(res):
                    res = s[l:r+1]

                removedChar = s[l]
                if removedChar in tFreq and winFreq[removedChar] == tFreq[removedChar]:
                    have -= 1
                winFreq[removedChar] -= 1
                
                l += 1
                # if remove one of the chars in tFreq, have - 1
                
                # check length of res
                # if not "" and shorter and thann current string store stringWindow in res
            
            # if have == need:
            #     if res == "":
            #         res = s[l:r+1] 
            #     elif (r - l + 1) < len(res):
            #         res = s[l:r+1]


        # whenever have == need
        # check length of res
        # if not "" and shorter and thann current string store stringWindow in res

        return res
        






