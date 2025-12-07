from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num: freq with Counter
        numFreq = Counter(nums)

        # list comprehension to return the keys of the most common k values
        return [num for num, _ in numFreq.most_common(k)]


