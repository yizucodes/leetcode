class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # Helper function to check if we can ship all packages 
        # within 'days' using ship capacity 'capacity
        def calculateDaysNeeded(weights, capacity):
                """
                Calculate how many days we need to ship all packages
                using the given capacity
                """
                daysNeeded = 1  # Start with first day
                currLoad = 0

                for w in weights:
                    if w > capacity:
                        return -1 # not possible to load

                    # Adding more load exceeds day
                    if currLoad + w > capacity:
                        daysNeeded += 1
                        currLoad = w
                    # currLoad < capacity
                    else:
                        currLoad += w
                    
                return daysNeeded


        # binary search
        l = max(weights)
        r = sum(weights)
        
        while l < r:
            # capacity
            m = (l + r) // 2 

            daysN = calculateDaysNeeded(weights, m)

            if daysN > days:
                l = m + 1
            else:
                r = m

        return l

