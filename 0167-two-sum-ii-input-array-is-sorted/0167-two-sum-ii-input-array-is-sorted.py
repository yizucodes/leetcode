class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Increase left if sum is smaller, decrease right if sum is larger

        left = 0
        right = len(numbers) - 1

        res = []

        while left < right:
            if (numbers[left] + numbers[right]) > target:
                right -= 1
            elif numbers[left] + numbers[right] == target:
                res.append(left + 1)
                res.append(right + 1)
                return res
            else:
                left += 1
        
        return res
            






        