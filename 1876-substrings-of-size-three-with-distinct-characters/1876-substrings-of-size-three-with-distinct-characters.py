class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isUnique(subString):
            if len(subString) == len(set(subString)):
                return True

            return False

        # 2 chars or less return 0 

        if len(s) <= 2:
            return 0
        
        res = 0
        # create a window of size 3 (last index is not inclusive)
        endIndex = 3
        for i in range(len(s)):
        # check substring from 0 to endIndex is unique
            charWindow = s[i:endIndex]
            if (isUnique(charWindow) and len(charWindow) == 3):
                res += 1
    
            # slide window by 1
            endIndex += 1

        return res
        