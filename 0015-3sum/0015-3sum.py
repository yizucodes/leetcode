class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to make it easier to find triplets and skip duplicates
        res = []

        # Iterate through the array
        for i in range(len(nums) - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]  # We need two numbers that sum to the negative of nums[i]
            left, right = i + 1, len(nums) - 1  # Set two pointers

            while left < right:
                currSum = nums[left] + nums[right]

                if currSum == target:
                    res.append([nums[i], nums[left], nums[right]])  # Found a valid triplet

                    # Skip duplicates for the second number (left pointer)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for the third number (right pointer)
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move pointers inward to continue searching for new pairs
                    left += 1
                    right -= 1
                elif currSum < target:
                    left += 1  # We need a larger sum, so move the left pointer to the right
                else:
                    right -= 1  # We need a smaller sum, so move the right pointer to the left

        return res
