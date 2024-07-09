class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        ans = 0
        exponent = 1
        while ans < n:
            ans = pow(2, exponent)
            if ans == n:
                return True
            exponent += 1
            
        return False
        