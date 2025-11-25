class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # If K is divisible by 2 or 5, no repunit works
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 0
        for n in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return n
        return -1