from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # num map
        numMap = Counter(nums)
        targetLen = len(nums) // 2

        # return number where its frequency is greater than n / 2
        for num in nums:
            freq = numMap[num]
            if freq > targetLen:
                return num

        return nums[0]
            



        