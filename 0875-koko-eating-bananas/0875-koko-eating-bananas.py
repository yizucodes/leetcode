from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # calculate hours

        def hours_needed(piles, k):
            hours = 0
            for pile in piles:
                hours += ceil(pile / k)

            return hours

        l = 1
        r = max(piles)

        while l < r:
            # Try a speed in the middle
            m = (l + r) // 2
            hoursNeeded = hours_needed(piles, m)

            # If that speed is too slow (takes > h hours): try faster speeds
            if hoursNeeded > h:
                l = m + 1
            # If that speed works (takes ≤ h hours): try slower speeds (looking for minimum)
            else:
                r = m

        
        return l
