class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # check for empty --> empty array
        left = 0
        n = len(numbers)
        right = n - 1
        
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum == target:
                # ensure to add 1 to both indices as it's one indexed
                return [left + 1, right + 1]
            elif currSum > target:
                right -= 1
            # currSum < target
            else:
                left += 1

        return res