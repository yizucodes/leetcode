class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleanS = ''.join(char for char in s if char.isalnum()).lower()

        if cleanS == "" or len(cleanS) == 1:
            return True

        startInd = 0
        endInd = len(cleanS) - 1

        while startInd < endInd:
            if cleanS[startInd] != cleanS[endInd]:
                return False

            startInd += 1
            endInd -= 1
        
        return True
        