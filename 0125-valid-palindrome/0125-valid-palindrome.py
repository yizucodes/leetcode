import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase
        lowerS = s.lower()
        # remove non-aplhanumber characters 
        lowerS = re.sub(r'[^a-zA-Z0-9]', '', lowerS)

        # for 1 or less size of s return True
        if len(lowerS) <= 1:
            return True

        left = 0
        right = len(lowerS) - 1

        # while loop until they meet at same index
        while left < right:
            if lowerS[left] != lowerS[right]:
                return False
            left += 1
            right -= 1

        return True