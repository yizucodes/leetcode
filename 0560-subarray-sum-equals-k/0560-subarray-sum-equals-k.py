class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        seen = {0:1}

        for num in nums:
            prefix += num

            # Check if there is prefix sum that if removed would give a subarray that sums to k
            if (prefix - k) in seen:
                count += seen[prefix - k]

                # Record prefix sum for future use
            if prefix in seen:
                seen[prefix] += 1
            else:
                seen[prefix] = 1
        return count





