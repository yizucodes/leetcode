from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num: freq with Counter
        numFreq = Counter(nums)

        # create array of { num: freq }  - list comprehension
        return [num for num, _ in numFreq.most_common(k)]


