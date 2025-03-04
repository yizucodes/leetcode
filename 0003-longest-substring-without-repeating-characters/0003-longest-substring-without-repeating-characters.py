class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l = 0
        r = 0
        max_len = 0

        char_set = set()

        while r < len(s):
            
            currChar = s[r]
            # If curr char not in set
            if s[r] not in char_set:
                char_set.add(currChar)
                r += 1
                max_len = max(max_len, r - l)

            # Duplicate
            else:
                char_set.remove(s[l])
                l += 1
        

    
        return max_len



