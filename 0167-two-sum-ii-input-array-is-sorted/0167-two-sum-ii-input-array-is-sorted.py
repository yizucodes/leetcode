class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            # if sum of l and r == target
            if (numbers[l] + numbers[r]) == target:
                return [l + 1, r + 1]

            # if sum > target:
            # move right pointer by 1 to the left
            elif (numbers[l] + numbers[r]) > target:
                r -= 1

            # if sum < target:
            # left pointer += 1
            else:
                l += 1

        # no solution
        return []
        
        
        