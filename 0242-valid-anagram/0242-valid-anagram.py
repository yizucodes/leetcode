class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a set and check if there are the same keys and values

        setS = {}

        for char in s:
            if char not in setS:
                setS[char] = 0
            else:
                currentVal = setS[char]
                setS[char] = currentVal + 1
        
        setT = {}

        for char in t:
            if char not in setT:
                setT[char] = 0
            else:
                currentVal = setT[char]
                setT[char] = currentVal + 1

        return setT == setS
        
        