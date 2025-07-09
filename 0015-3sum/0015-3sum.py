class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # fix first number
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            # 2 pter for remaining
            l, r = i + 1, len(nums) - 1

            # 2 pter
            while l < r:
                treSum = a + nums[l] + nums[r]

                if treSum > 0:
                    r -= 1
                elif treSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                
                # skip duplicates for second number
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

        return res

        