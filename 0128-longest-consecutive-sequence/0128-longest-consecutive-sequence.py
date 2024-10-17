class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
    
        # Nums to set
        numSet = set(nums)
        res = 0
        # Find starting number from set, start - 1 does not exist (left neighbor is inexistent)
        for num in nums:
            # check if it has left neighbor in set
            leftN = num - 1
            # if no left neighbor , that means number is start of sequence
            if leftN not in numSet:
                # If there is right neighbor, continue checking until there is no longer right neighbor
                currNum = num + 1
                lenSeq = 0
                while True:
                    if currNum in numSet:
                        lenSeq += 1
                        currNum += 1
                    # reached end of sequence
                    else:
                        lenSeq += 1
                        res = max(res, lenSeq)
                        break

        return res

        