class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non letters and numbers
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
        # trim spacing
        cleaned = cleaned.strip()
        # lowercase everything
        cleaned = cleaned.lower()

        l = 0
        r = len(cleaned) - 1

        if len(cleaned) <= 1:
            return True

        # iterate as long as they are 
        while l < r:
            print('left', l)
            print('right', r)
            if cleaned[r] == cleaned[l]:
                l += 1
                r -= 1
            else:
                return False
            
        # move right by 1 and left by 1 
        # if right and left match then it's a palindrome
        return True