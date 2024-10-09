class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        numsSorted = sorted(nums)
      

        for i in range(len(numsSorted)):
            if i > 0 and numsSorted[i] == numsSorted[i - 1]:
                continue
            left = i + 1

            right = len(numsSorted) - 1
            while left < right:
                tempSum = numsSorted[i] + numsSorted[left] + numsSorted[right]
                if tempSum == 0:
                    res.append([numsSorted[i], numsSorted[left], numsSorted[right]])

                    # Skip duplicates for left and right
                    while left < right and numsSorted[left] == numsSorted[left + 1]:
                        left += 1
                    while left < right and numsSorted[right] == numsSorted[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif tempSum < 0:
                    left += 1
                elif tempSum > 0:
                    right -= 1


        return res

