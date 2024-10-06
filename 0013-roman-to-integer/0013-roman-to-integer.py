class Solution:
    def romanToInt(self, s: str) -> int:

        # map each symbol to value
        numMap = { 'I': 1, 'V' : 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        
        total = 0

        for i in range(len(s)):
            # get integer value from map
            char = s[i]
            currVal = numMap[char]
            nextVal = 0
            if (i + 1) < len(s):
                nextVal = numMap[s[i + 1]]

            # compare current numberal value with value of next numerical value if any
            if currVal < nextVal:
                
                # if current val < next val, subtract current val from total
                total -= currVal

                # else add current val to total
            else: 
                total += currVal


        return total