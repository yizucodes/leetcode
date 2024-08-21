class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        # if one letter or the entire string has one distict character (e.g. "bbbbbbb")
        if len(s) == 1 or len(set(s)) == 1: 
            return 1

        maxLength = 0
        left = 0 
        right = 0
        tempSet = set()
        
        while right < len(s):
          
            tempLength = 0
            # move right pointer as long as there is a unique character
            if s[right] not in tempSet:
                tempSet.add(s[right])
                
                currWindowSize = right - left + 1

                if currWindowSize > maxLength:
                    maxLength = currWindowSize
                right += 1
            
            else:
                tempSet.remove(s[left])
                left += 1
            
        return maxLength


