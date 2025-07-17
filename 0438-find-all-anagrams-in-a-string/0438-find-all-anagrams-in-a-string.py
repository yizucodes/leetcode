class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # if p is empty --> return []

        # p is shorter than s 

        l = 0
        r = len(p) - 1
        res = []
        while r < len(s):
            window = s[l : r + 1] # array
            
            if Counter(window) == Counter(p):
                res.append(l)
            
            l += 1
            r += 1

        
        return res