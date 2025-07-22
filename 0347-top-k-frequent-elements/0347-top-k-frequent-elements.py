from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        # {1: 3, 2: 2, 3: 1}

        numMap = Counter(nums)

        # Step 2: Sort by frequency (somehow)
        # [(1, 3), (2, 2), (3, 1)]  # (element, frequency) pairs
        mostCommon = numMap.most_common(k)

        # Step 3: Take top k elements
        # Return [1, 2]
        res = [element for element, freq in mostCommon]
        return res