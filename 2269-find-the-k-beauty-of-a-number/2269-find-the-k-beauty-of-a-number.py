class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        if k > len(str(num)):
            return 0

        # put into string
        numStr = str(num)
        res = 0
        currWindow = int(numStr[:k])
    

        for i in range(len(numStr) - k + 1):
        # check if num / window gives modulo 0
        # yes then res += 1

            # slide window
            currWindow = int(numStr[i:i+k])

            if currWindow != 0 and num % currWindow == 0 :
                res += 1

        return res
        



