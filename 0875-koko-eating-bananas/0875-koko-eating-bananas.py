from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # function that determines if can eat within limit (h)
        def hoursNeeded(piles, speed):
            hours = 0
            for pile in piles:
                hours = ceil(pile / speed) + hours
            return hours        

        # binary search
        l = 1
        r = max(piles)

        while l < r:
        
            m = (l + r) // 2

            hrsNeeded = hoursNeeded(piles, m)

            # hoursNeeded > h --> try finding higher number for speed
            if hrsNeeded > h:
                l = m + 1
            # if less hours --> try finding lower speed if possible to meet minimum
            # hoursNeeded <= h -->
            else:
                r = m
                
        return l


