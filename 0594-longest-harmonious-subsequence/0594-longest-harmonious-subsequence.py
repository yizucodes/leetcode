from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # if len is 1 return 0
        if len(nums) == 1:
            return 0

        # Count freq of each element in array
        freq = Counter(nums)
        maxLength = 0

        # Iterate through frequency dictionary
        for num in freq:

            # Check if next consecutive number exists 
            if num + 1 in freq:
                # Add frequencies of num and num + 1
                maxLength = max(maxLength, freq[num] + freq[num + 1])
        
        return maxLength
